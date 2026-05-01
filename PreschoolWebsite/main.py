from flask import Flask, render_template, request, redirect, url_for
from forms import ContactForm
import smtplib
import os

SET_LANGUAGE = "english"

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv("SECRET_KEY") #this doesn't connect to the .env file but it makes deploying possible

def send_email(from_name, from_email, content):
    my_email = "alikor23@gmail.com"
    password = "cszp lare ojeq xobv"

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()  # Transport Layer Security
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=my_email,
                            msg=f"Subject:Message from Soyo Kaze Website Visitor\n\n{content}\n\n{from_name}\n{from_email}")

@app.route("/", methods=["GET","POST"])
def open_home_page():
    print(f"Page: {request.args.get("page")}, Method: {request.method}, Language: {request.args.get("language")}")
    if request.method == "GET":
        return render_template("index.html", page='home')
    else:
        if request.args.get("language") == 'japanese':
            return render_template("index_jp.html", page='home')
        else:
            return render_template("index.html", page='home')

# @app.route("/jp", methods=["GET","POST"])
# def open_home_page_jp():
#     return render_template("index_jp.html", page='home')

@app.route("/hiring", methods=["GET","POST"])
def open_job_page():
    print(f"Page: {request.args.get("page")}, Method: {request.method}, Language: {request.args.get("language")}")
    if request.method == "GET":
        return render_template("job.html", page="hiring")
    else:
        if request.args.get("language") == 'japanese':
            return render_template("job_jp.html", page='hiring')
        else:
             return render_template("job.html", page="hiring")


# @app.route("/hiring/jp", methods=["GET","POST"])
# def open_job_page_jp():
#     return render_template("job_jp.html", page="hiring")

@app.route("/schedule", methods=["GET","POST"])
def open_schedule_page():
    print(f"Page: {request.args.get("page")}, Method: {request.method}, Language: {request.args.get("language")}")
    if request.method == "GET":
        return render_template("schedule.html", page="schedule")
    else:
        if request.args.get("language") == 'japanese':
            print(request.method)
            return render_template("schedule_jp.html", page="schedule")
        else:
            return render_template("schedule.html", page="schedule")


# @app.route("/schedule/jp", methods=["GET","POST"])
# def open_schedule_page_jp():
#     return render_template("schedule_jp.html", page="schedule")

@app.route("/contact", methods=["GET","POST"])
def open_contact_page():
    print(f"Page: {request.args.get("page")}, Method: {request.method}, Language: {request.args.get("language")}")
    if request.method == "GET":
        return render_template("contact.html", method="GET", page="contact")
    else:
        try:
            if request.form["name"]:
                send_email(request.form["name"], request.form["email"], request.form["message"])
                return render_template("confirmation.html", method="POST")
        except KeyError:
            if request.args.get("language") == 'japanese':
                return render_template("contact_jp.html", page="contact")
            else:
                return render_template("contact.html", page="contact")

# @app.route("/contact/jp", methods=["GET","POST"])
# def open_contact_page_jp():
#     if request.method == "GET":
#         return render_template("contact_jp.html", method="GET", page="contact")
#     else:
#         send_email(request.form["name"], request.form["email"], request.form["message"])
#         return render_template("confirmation_jp.html", method="POST")

# @app.route("/success", methods=["POST"])
# def open_success_page():
#     return render_template("confirmation.html", method="POST")

@app.route("/language", methods=["POST"])
def open_language_page():
    if request.form.get("language") == 'japanese':
        print(f"Language requested: {request.args.get('language')}; Site requested: {request.args.get('page')}")
        if request.args.get("page") == 'home':
            return redirect(url_for("open_home_page", language = "japanese"), code=307)
        elif request.args.get("page") == 'schedule':
            return redirect(url_for("open_schedule_page", language = "japanese"), code=307)
        elif request.args.get("page") == 'hiring':
            return redirect(url_for("open_job_page", language = "japanese"), code=307)
        elif request.args.get("page") == 'contact':
            return redirect(url_for("open_contact_page", language = "japanese"), code=307)
    else:
        if request.args.get("page") == 'home':
            return redirect(url_for("open_home_page"))
        elif request.args.get("page") == 'schedule':
            return redirect(url_for("open_schedule_page"))
        elif request.args.get("page") == 'hiring':
            return redirect(url_for("open_job_page"))
        elif request.args.get("page") == 'contact':
            return redirect(url_for("open_contact_page"))


if __name__ == '__main__':
    app.run(debug=True) #this is like >flask run

