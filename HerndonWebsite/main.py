from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv("SECRET_KEY") #this doesn't connect to the .env file but it makes deploying possible

class Base(DeclarativeBase):
  pass

db = SQLAlchemy(model_class=Base)

# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///herndon_cafes.db"
# initialize the app with the extension
db.init_app(app)

class Cafe(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    map_url: Mapped[str] = mapped_column(String(500), nullable=False)
    img_url: Mapped[str] = mapped_column(String(500), nullable=False)
    location: Mapped[str] = mapped_column(String(250), nullable=False)
    phone: Mapped[str] = mapped_column(String(250), nullable=False)
    hours: Mapped[str] = mapped_column(String(250), nullable=False)
    has_food: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=False)
    is_spacious: Mapped[bool] = mapped_column(Boolean, nullable=False)
    can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=False)

with app.app_context():
    db.create_all()
    db.session.commit()

def filter_items(new_list, old_list, amenity):
    for item in old_list:
        if not getattr(item, amenity):
            try:
                new_list.remove(item)
            except ValueError:
                pass

def filter_cafes(filters, cafes_all):
    cafes_filtered = cafes_all.copy()
    for toggle_state in filters:
        if toggle_state.count('wifi') > 0:
            filter_items(new_list=cafes_filtered, old_list=cafes_all, amenity="has_wifi")
        if toggle_state.count('socket') > 0:
            filter_items(new_list=cafes_filtered, old_list=cafes_all, amenity="has_sockets")
        if toggle_state.count('spacious') > 0:
            filter_items(new_list=cafes_filtered, old_list=cafes_all, amenity="is_spacious")
        if toggle_state.count('food') > 0:
            filter_items(new_list=cafes_filtered, old_list=cafes_all, amenity="has_food")
        if toggle_state.count('toilet') > 0:
            filter_items(new_list=cafes_filtered, old_list=cafes_all, amenity="has_toilet")
        if toggle_state.count('call') > 0:
            filter_items(new_list=cafes_filtered, old_list=cafes_all, amenity="can_take_calls")
    return cafes_filtered

def add_site(locname, maplink, imglink, addr, ph, hrs, food, toilet, wifi, socket, spacious, call):
    with app.app_context():
        new_site = Cafe(name=locname, map_url=maplink, img_url=imglink, location=addr, phone=ph, hours=hrs, has_food=food, has_toilet=toilet, has_wifi=wifi, has_sockets=socket, is_spacious=spacious, can_take_calls=call)
        db.session.add(new_site)
        db.session.commit()

def delete_site(site_name):
    with app.app_context():
        result = db.session.execute(db.select(Cafe).filter_by(name=site_name)).scalar_one()
        site_to_delete = db.get_or_404(Cafe, int(result.id))
        db.session.delete(site_to_delete)
        db.session.commit()

@app.route('/', methods=["GET", "POST"])
def home():
    result = db.session.execute(db.select(Cafe))
    cafes = result.scalars().all()
    if request.method == "GET":
        print("Get method")
        return render_template("index.html", all_places = cafes, toggles = [])
    else:
        toggle_state = request.form.getlist('filters')
        if toggle_state:
            print(toggle_state)
            cafes_filtered = filter_cafes(filters = toggle_state, cafes_all = cafes)
            return render_template("index.html", all_places = cafes_filtered, toggles = toggle_state)
        else:
            return render_template("index.html", all_places=cafes, toggles=toggle_state)

@app.route('/search', methods=["POST"])
def search():
    result = db.session.execute(db.select(Cafe))
    cafes = result.scalars().all()
    cafe_select = []
    print(cafes)
    for cafe in cafes:
        print(request.form.get('site_name').lower())
        print(cafe.name.lower())
        if cafe.name.lower() == request.form.get('site_name').lower():
            cafe_select.append(cafe)
    if cafe_select:
        return render_template("searchresult.html", all_places=cafe_select)
    else:
        return redirect(url_for("home"))

@app.route('/addsite', methods=["GET","POST"])
def add():
    if request.method == "GET":
        return render_template("addsite.html")
    else:
        if request.form.get('has_food'):
            food = True
        else:
            food = False
        if request.form.get('has_sockets'):
            socket = True
        else:
            socket = False
        if request.form.get('has_wifi'):
            wifi = True
        else:
            wifi = False
        if request.form.get('has_toilet'):
            toilet = True
        else:
            toilet = False
        if request.form.get('is_spacious'):
            spacious = True
        else:
            spacious = False
        if request.form.get('can_take_calls'):
            call = True
        else:
            call = False
        add_site(locname=request.form.get('place_name'),
                 maplink=request.form.get('map_url'),
                 imglink=request.form.get('img_url'),
                 addr=request.form.get('address'),
                 ph=request.form.get('phonenumber'),
                 hrs=request.form.get('hours'),
                 toilet=toilet,
                 wifi=wifi,
                 socket=socket,
                 food=food,
                 spacious=spacious,
                 call=call
                 )
        return render_template("confirmation.html")

@app.route('/confirmation', methods=["GET"])
def confirm_add():
    return render_template("confirmation.html")

##NOTE THAT BROWSERS ONLY SUPPORT GET AND POST REQUESTS -> HENCE A BROWSER CALL TO DELETE A SITE WON'T WORK.
##THE DATA WOULD NEED TO BE ACCESSED USING AN API CALL - THIS CAN BE TESTED IN POSTMAN!


#API DELETE METHOD
@app.route('/delete/<name>', methods=["DELETE"])
def delete(name):
    entered_api_key = request.args.get("api-key")
    print(entered_api_key)
    if entered_api_key == "abcdefg":
        try:
            delete_site(name)
        except AttributeError:
            return jsonify({"error": {"Not Found": "Sorry, we don't have a site with that name in the database."}}), 404
        else:
            return jsonify({"success": "Successfully deleted the site."}), 200
    else:
        return jsonify(error={"Forbidden": "Sorry, that's not allowed. Make sure you have the correct api_key."}), 403

#BROWSER DELETE METHOD
@app.route('/delete_site/<name>', methods=["GET", "POST"])
def delete_from_browser(name):
    delete_site(name)
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True,port=5088)

