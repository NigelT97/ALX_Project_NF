"""
This script runs the application using a development server.
It contains the definition of routes and views for the application.
"""

from ensurepip import bootstrap
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database_NF.db'
db = SQLAlchemy(app)

# Make the WSGI interface available at the top level so wfastcgi can get it.
wsgi_app = app.wsgi_app

@app.route('/')
def home():
    """Renders a sample page."""
    return render_template('MainPage.html')

@app.route('/ProductPage')
def ProdPage():
    """Renders the Production Page."""
    return render_template('ProductPage.html')

@app.route('/FullQuotePage')
def FullQPage():
    """Renders the Production Page."""
    return render_template('FullQuotePage.html')

@app.route('/About')
def AboutPage():
    """Renders the Production Page."""
    return render_template('AboutPage.html')

if __name__ == '__main__':
    import os
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(os.environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT)
