from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

db = SQLAlchemy()
migrate = Migrate(compare_type=True)
login_manager = LoginManager()

def create_app():

    app = Flask(__name__)
    app.config.from_pyfile('../config.py')
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    login_manager.login_view = "auth.login"

    from . import auth, book, rental

    app.register_blueprint(auth.bp)
    app.register_blueprint(book.bp)
    app.register_blueprint(rental.bp)

    @app.route('/')
    def hello_world():

        from .forms import LoginForm
        form = LoginForm()

        return render_template('auth/index.html', form=form)

    return app
