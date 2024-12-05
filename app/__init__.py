from flask import Flask
from flask_assets import Bundle, Environment


def create_app():
    app = Flask(__name__)

    # Configure app
    app.config["SECRET_KEY"] = "dev"  # Change this in production

    # Initialize Flask-Assets
    assets = Environment(app)

    # Bundle and compress CSS files
    css = Bundle(
        "css/tailwind.css", filters="cssmin", output="dist/css/main.css"
    )
    assets.register("css_all", css)

    # Register blueprints
    from app.main import bp as main_bp

    app.register_blueprint(main_bp)

    return app
