from diet_planner import db


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    calories = db.Column(db.Integer)