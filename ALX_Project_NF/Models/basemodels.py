"""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Users(db.Model):
       __tablename__ = 'users'
       id = db.Column(db.Integer, primary_key = True)
       name = db.Column(db.String(200), nullable = False)
       email = db.Column(db.String(120), nullable = False, unique = True)
       password = db.Column(db.String(120), nullable = False)
       
class ProductTable(db.Model):
       __table__ = 'products'
       id = db.Column(db.Integer, primary_key = True)
       name = db.Column(db.String(200), nullable = False)
       Description = db.Column(db.String(200), nullable = False)
       Price = db.Coulmn(db.DECIMAL(10, 2), nullable = False)

"""
