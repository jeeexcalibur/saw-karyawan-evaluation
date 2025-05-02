# config.py

class Config:
    SECRET_KEY = 'super-secret-key'
    SQLALCHEMY_DATABASE_URI = 'postgresql://Mikoto:0@localhost:5432/saw_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
