from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Inisialisasi database
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    # Konfigurasi aplikasi
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:password@127.0.0.1:3308/sdlc_programmer'
    # SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://root:password@host.docker.internal:3308/sdlc_programmer"
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:@db:3306/sdlc_programmer'

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.secret_key = 'your_secret_key'

    # Inisialisasi ekstensi
    db.init_app(app)

    # Import dan daftar blueprint
    from .routes import main
    app.register_blueprint(main)

    return app
