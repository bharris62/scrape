from flask import Flask, render_template, redirect
from database import session
from database import Product


app = Flask(__name__)


@app.route("/")
def home():
    products = session.query(Product).all()
    return render_template('base.html',
                           products=products)


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)