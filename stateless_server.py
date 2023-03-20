import os

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

# create Flask app
app = Flask(__name__)

# configure the app to use SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL")

# disable the modification tracking system to save resources
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# initialize SQLAlchemy
db = SQLAlchemy(app)

# define the User model with the required columns
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(50))

    # define a method to convert User object to a dictionary
    def to_dict(self):
        return {'id': self.id, 'name': self.name, 'email': self.email, 'password': self.password}

with app.app_context():
    db.create_all()

# define a route to create a new user
@app.route('/users', methods=['POST'])
def create_user():
    # get the data from the request body
    data = request.get_json()

    # create a new User object using the data
    user = User(name=data['name'], email=data['email'], password=data['password'])

    # add the user to the session
    db.session.add(user)

    # commit the changes to the database
    db.session.commit()

    # return the user as a dictionary with status code 201 (created)
    return jsonify(user.to_dict()), 201

# define a route to get all users
@app.route('/users', methods=['GET'])
def get_users():
    # query all the User objects from the database
    users = User.query.all()

    # return a list of user dictionaries
    return jsonify([user.to_dict() for user in users])

# define a route to get a specific user by ID
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    # query the User object with the given ID from the database
    user = User.query.get(user_id)

    # if the user exists, return the user as a dictionary
    if user:
        return jsonify(user.to_dict())

    # if the user does not exist, return an error dictionary with status code 404 (not found)
    return jsonify({'error': 'User not found'}), 404

# define a route to update a specific user by ID
@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    # query the User object with the given ID from the database
    user = User.query.get(user_id)

    # if the user does not exist, return an error dictionary with status code 404 (not found)
    if not user:
        return jsonify({'error': 'User not found'}), 404

    # get the data from the request body
    data = request.get_json()

    # update the user object with the new data
    user.name = data.get('name', user.name)
    user.email = data.get('email', user.email)
    user.password = data.get('password', user.password)

    # commit the changes to the database
    db.session.commit()

    # return the updated user as a dictionary
    return jsonify(user.to_dict())

# define a route to delete a specific user by ID
@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    # query the User object with the given ID from the database
    user = User.query.get(user_id)

    # if the user does not exist, return an error dictionary with status code 404 (not found)
    if not user:
        return jsonify({'error': 'User not found'}), 404

    # delete the user from the session
    db.session.delete(user)

    # commit the changes to the database
    db.session.commit()

    # return an empty response with status code 204 (no content)
    return '', 204

# run the app
if __name__ == 'main':
    app.run(debug=False)


