from flask import Flask, render_template, redirect, url_for, request, flash
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from forms import *
import flask_wtf as wtf

# create the extension

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)

##CONNECT TO DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:/Users/becke/PycharmProjects/Day 87/cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    wifi_strength = db.Column(db.Integer, nullable=False)
    outlets = db.Column(db.Boolean, nullable=True)
    location = db.Column(db.String, nullable=False)
    img = db.Column(db.String, nullable=False)

    def __init__(self, id, name, wifi_strength, outlets, location, img, rating):
        __tablename__ = "cafes"
        self.id = id
        self.name = name
        self.wifi_strength = wifi_strength
        self.outlets = outlets
        self.location = location
        self.img = img
        self.rating = rating


@app.route("/")
def home_page():
    cafes = Cafe.query.all()
    print(cafes)
    return render_template("index.html", cafes=cafes)


@app.route("/add", methods=["GET", "POST"])
def add_cafe():
    cafe_form = CafeForm()
    if request.method == "GET":
        return render_template("add_cafe.html", form=cafe_form)
    elif request.method == "POST":
        new_name = cafe_form.name.data
        new_rating = int(cafe_form.rating.data)
        new_location = cafe_form.location.data
        new_outlets = cafe_form.outlets.data
        new_wifi = int(cafe_form.wifi_strength.data)
        new_img = cafe_form.img_url.data
        cafe_id = len(Cafe.query.all()) + 1
        new_cafe = Cafe(name=new_name, rating=new_rating, location=new_location, outlets=new_outlets, wifi_strength=new_wifi, img=new_img, id=cafe_id)
        with app.app_context():
            db.session.add(new_cafe)
            db.session.commit()
        flash(f"{new_name} was successfully added")
        return redirect(url_for("home_page"))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)