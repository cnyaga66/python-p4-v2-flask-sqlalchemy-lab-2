from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy_serializer import SerializerMixin


metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db = SQLAlchemy(metadata=metadata)


class Customer(db.Model):
    __tablename__ = 'customers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

    Review = Review(back_populates=Review)

    def __repr__(self):
        return f'<Customer {self.id}, {self.name}>'


class Item(db.Model):
    __tablename__ = 'items'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    price = db.Column(db.Float)

    Review = Review(back_populates=Review)

    def __repr__(self):
        return f'<Item {self.id}, {self.name}, {self.price}>'
    
class Review(db.Model):
    __tablename__ = 'reviews'
    
    id =  db.Column (db.comment)
    customer_id = db.Column(db.Integer, db.ForeignKey('customers.id'), primary_key=True)
    item_id = db.Column(db.Integer, db.ForeignKey('items.id'), primary_key=True)
    review = db.Column(db.String)

    Customer = Customer(back_populates=Customer)
    Item = Item(back_populates=Item)

    
    
