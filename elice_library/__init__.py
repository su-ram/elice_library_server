from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate(compare_type=True)

def create_app():

    app = Flask(__name__)
    app.config.from_pyfile('../config.py')
    db.init_app(app)
    migrate.init_app(app, db)

    from . import auth, book, rental

    app.register_blueprint(auth.bp)
    app.register_blueprint(book.bp)
    app.register_blueprint(rental.bp)

    @app.route('/')
    def hello_world():

        from .login_form import LoginForm
        form = LoginForm()

        return render_template('auth/index.html', form=form)

    return app
