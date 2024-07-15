from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixing
db = SQLAlchemy()
class Customer(db.Model):
    __tablename__ = 'customers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

    Review = db.relationship('Review',back_populates='customer')
    items = association_proxy('reviews', 'item')
    serialize_rules = ('-reviews.customer',)
class Item(db.Model):
    __tablename__ = 'items'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    price = db.Column(db.Float)

    review =db.relationship('Review', back_populates='item')
    serialize_rules = ('-reviews.item',)
class Review(db.Model):
    __tablename__ = 'reviews'
    id =  db.Column(db.Integer, primary_key=True)
    comment = db.Column(db.String(255), nullable=False)
    customer_id = db.Column(db.Integer, db.ForeignKey('customers.id'))
    item_id = db.Column(db.Integer, db.ForeignKey('items.id'), )
    Customer = Customer(back_populates=Customer)
    review = db.Column(db.String)
    serialize_rules = ('-customer.reviews',-item.reviews)
