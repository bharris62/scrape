import os

from flask import Flask, render_template, redirect
from datetime import datetime, timedelta

from supps.extensions import db
from supps.models import Product


BASE_PATH = os.path.join(os.path.abspath(os.path.dirname(__file__)), '..')


def create_app(package_name, settings_override=None):
    """
    This is a starter function for using the Flask application factory pattern.

    :param settings_override: settings to override the default
    :param package_name: typically __name__ for the package_name
    :return: the application instance
    """

    app = Flask(__name__, instance_relative_config=True)

    # For local
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://BHarris:@localhost:5432/supplements'

    # For Heroku

    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']

    if settings_override:
        app.config.from_object(settings_override)


    # Init extensions
    db.init_app(app)

    # You'll want to probably turn this into a blueprint eventually.
    # http://flask.pocoo.org/docs/0.11/blueprints/#blueprints
    @app.route("/")
    def home():
        products = db.session.query(Product).filter(Product.product_type == 'Protein').order_by(Product.product_price_per_serving).filter(Product.last_update >= (datetime.utcnow() - timedelta(hours=3))).limit(10)
        return render_template('base.html',
                               products=products,
                               is_active = 'active',
                               type_product='Top 10 Cheapest Proteins')

    @app.route("/whey")
    def whey():
        products = db.session.query(Product).filter(Product.product_type == 'Protein').order_by(Product.product_price_per_serving).filter(Product.last_update >= (datetime.utcnow() - timedelta(hours=3)))
        return render_template('base.html',
                               products=products,
                               type_product='Find best Prices on Protein')

    @app.route("/casein")
    def casein():
        products = db.session.query(Product).order_by(Product.product_price_per_serving).filter(Product.last_update >= (datetime.utcnow() - timedelta(hours=3)))
        return render_template('base.html',
                               products=products,
                               type_product='Find best Prices on Casein')

    @app.route("/preworkout")
    def preworkout():
        products = db.session.query(Product).filter(Product.product_type == 'Pre-Workout').order_by(Product.product_price_per_serving).filter(Product.last_update >= (datetime.utcnow() - timedelta(hours=3)))
        return render_template('base.html',
                               products=products,
                               is_active='active',
                               type_product='Find best Prices on Pre Workout')

    @app.route("/vitamin")
    def vitamin():
        products = db.session.query(Product).filter(Product.product_type == 'Vitamin').order_by(Product.product_price_per_serving).filter(Product.last_update >= (datetime.utcnow() - timedelta(hours=3)))
        return render_template('base.html',
                               products=products,
                               type_product='Find best Prices on Vitamins')

    @app.route("/postworkout")
    def postworkout():
        products = db.session.query(Product).filter(Product.product_type == 'Post-Workout').order_by(Product.product_price_per_serving).filter(Product.last_update >= (datetime.utcnow() - timedelta(hours=3)))
        return render_template('base.html',
                               products=products,
                               type_product='Find best Prices on Post Workout')

    @app.route("/beta")
    def beta():
        products = db.session.query(Product).order_by(Product.product_price_per_serving).filter(Product.last_update >= (datetime.utcnow() - timedelta(hours=3)))
        return render_template('base.html',
                               products=products)

    @app.route("/pages/<page>")
    def page(page):
        page = page +'.html'
        return render_template(page)
    return app
