from datetime import datetime

from .extensions import db


class Product(db.Model):
    """
    Creates products table, holds information; will hold various products, from
    various websites
    """
    __tablename__ = 'products'

    id = db.Column(db.Integer, primary_key=True)
    product_dealer = db.Column(db.String)
    product_name = db.Column(db.String)
    product_url = db.Column(db.String)
    product_price = db.Column(db.String)
    product_price_per_serving = db.Column(db.String)
    product_type = db.Column(db.String)
    product_image = db.Column(db.String)
    product_description = db.Column(db.String)
    last_update = db.Column(db.DateTime, default=datetime.utcnow)

