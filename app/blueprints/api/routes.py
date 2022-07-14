from flask import jsonify, request, redirect
from . import bp as app
from app.blueprints.main.models import Car
from app import db



@app.route("/car_update", methods=["POST"])
def car_update():
    
    carMakeInput = request.form["carMakeInput"]
    modelInput = request.form["carModelInput"]
    yearInput = request.form["carYearInput"]
    colorInput = request.form["carColorInput"]
    priceInput = request.form["carPriceInput"]
    user = 1
    

    new_car = Car(make=carMakeInput, model=modelInput, year=yearInput, color=colorInput, price=priceInput, user_id=user)
    db.session.add(new_car)
    db.session.commit()
    
    return  redirect("http://127.0.0.1:5000")