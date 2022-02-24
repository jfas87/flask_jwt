import os
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def init_db(app):
    
    bd_dir = os.path.abspath(os.path.dirname(__file__))
    app.config['SQLALCHEMY_DATABASE_URI']  = "sqlite:///" + os.path.join(bd_dir, 'app.db')
    db.init_app(app)

    with app.app_context():
        db.create_all()
