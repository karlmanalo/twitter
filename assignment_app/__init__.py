# assignment_app\__init__.py

from flask import Flask
from assignment_app.models import db, migrate
from assignment_app.routes.tweet_routes import tweet_routes
from assignment_app.routes.home_routes import home_routes


def create_app():
    app = Flask(__name__)

    DATABASE_URI = "sqlite:///C:\\Users\\Karl\\Documents\\lambda\\u3s3\\twitter\\twitter.db"

    app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URI
    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(tweet_routes)
    app.register_blueprint(home_routes)
    return app

if __name__ == "__main__":
    twitter_app = create_app()
    twitter_app.run(debug=True)
