from flask import Flask, jsonify, render_template, request
from sam_gov import SamSearch
from federal_agencies import AgencyEndpoints

app = Flask(__name__)

search = SamSearch()
agencies = AgencyEndpoints()

@app.route("/", methods=["GET"])
def home():
    endpoints = agencies.get_agency_endpoints()
    return render_template("index.html", endpoints = endpoints)

@app.route("/<agency_name>", methods=["GET"])
def retrieve_data(agency_name):
    agency_data = search.search_most_visits(agency_name=agency_name)
    if agency_data:
        return jsonify(agency_data)

@app.route("/<agency_name>/2026", methods=["GET"])
def retrieve_filtered_data(agency_name):
    agency_data = search.search_all_visits(agency_name=agency_name)
    limit = request.args.get("limit", type = int)
    if limit:
        agency_data_trunc = agency_data[:limit]
        return jsonify(agency_data = agency_data_trunc)
    else:
        return jsonify(agency_data= agency_data)

if __name__ == '__main__':
    app.run(debug=True)