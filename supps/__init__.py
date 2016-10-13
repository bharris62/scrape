from supps import app


def create_app():
    return app.create_app(__name__)
