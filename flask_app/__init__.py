from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config.from_object('flask_app.config.Config')

    from flask_app.routes.routes import routes
    app.register_blueprint(routes)

    return app
