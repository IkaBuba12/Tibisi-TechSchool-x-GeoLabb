from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'jdchuijwosnchhjnd'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.database'

db = SQLAlchemy(app)
