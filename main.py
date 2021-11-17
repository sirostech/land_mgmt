from flask import Flask, request
from flask_restful import Resource, Api
from src.routes import *
import requests
import os
from flask import Flask, render_template

app = Flask(__name__)
api = Api(app)


api.add_resource(Owners, '/api/owners')
api.add_resource(Units, '/api/units')
api.add_resource(OwnersByUnit, '/api/units/<int:id>/owners')
api.add_resource(CreateOwner, '/api/create_owner')
api.add_resource(CreateUnit, '/api/create_unit')
api.add_resource(CreateUnitOwner, '/api/create_unit_owner')
api.add_resource(DeleteUnitOwner, '/api/delete_unit_owner')


@app.route("/owners")
def owner_index():
    data = requests.get("http://localhost:5000/api/owners")

    return render_template("owners/index.html", message=data.json());


@app.route("/units")
def unit_index():
    data = requests.get("http://localhost:5000/api/units")

    return render_template("units/index.html", message=data.json());


@app.route("/")
def test():
    return render_template("/welcome/index.html");


if __name__ == '__main__':
    app.run(debug=True)
