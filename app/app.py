from flask import Flask, jsonify
# ModuleNotFoundError: No module named 'flask_cors' = pip install Flask-Cors
from flask_cors import CORS, cross_origin
from models import db, Users

app = Flask(__name__)

app.config['SECRET_KEY'] = 'cairocoders-ednalan'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///flaskdb.db'
# Databse configuration mysql                             Username:password@hostname/databasename
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:''@localhost/flaskreact'

SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_ECHO = True

CORS(app, supports_credentials=True)

db.init_app(app)

with app.app_context():
    db.create_all()


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route('/users', methods=['GET'])
def users():

    total = Users.query.count()

    userdata = Users.query.order_by(Users.id.asc()).all()

    return jsonify({
        'total': total,
        'results': [{
            'id': rs.id,
            'name': rs.name,
            'email': rs.email,
            'password': rs.password
        } for rs in userdata]
    })


if __name__ == "__main__":
    app.run(debug=True)
