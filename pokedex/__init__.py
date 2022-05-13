from flask import Flask


def create_app(test_config=None):
    app = Flask(__name__)

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile("config.py", silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # simple page that says hello
    @app.route("/hello")
    def hello():
        return "Hello, world!"

    from . import pokemon

    app.register_blueprint(pokemon.bp)

    return app
