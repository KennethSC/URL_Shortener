from flask import Flask

def create_app(test_config=None):
    app = Flask(__name__)
    app.secret_key = '78h377y87y&*&Y&Y78yY*^G^G^&g'

    from . import urlshort

    app.register_blueprint(urlshort.bp)

    return app