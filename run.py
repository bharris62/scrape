from flask import Flask, render_template
from database import session
from database import Product


app = Flask(__name__)


@app.route("/")
def home():
    product_name = session.query(Product.product_name).first()
    product_image = session.query(Product.product_image).first()
    price_per_serving = session.query(Product.product_price_per_serving).first()
    product_price = session.query(Product.product_price).first()
    product_type = session.query(Product.product_type).first()
    product_description = session.query(Product.product_description).first()
    return render_template('base.html',
                           product_name=product_name[0],
                           product_image=product_image[0],
                           price_per_serving=price_per_serving[0],
                           product_price=product_price[0],
                           product_type=product_type[0],
                           product_description=product_description[0])


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=8080)