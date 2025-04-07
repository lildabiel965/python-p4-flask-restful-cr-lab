from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy import Numeric

db = SQLAlchemy()

class Plant(db.Model, SerializerMixin):
    __tablename__ = 'plants'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    image = db.Column(db.String)
    price = db.Column(Numeric(precision=10, scale=2))
