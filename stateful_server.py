from flask import Flask, request, jsonify

# create Flask app
app = Flask(__name__)

# initialize an empty list to hold users data
users = []

# define a route to create a new user
@app.route('/users', methods=['POST'])
def create_user():
    # get the data from the request body
    data = request.get_json()

    # create a new user dictionary using the data
    user = {'id': len(users) + 1, 'name': data['name'], 'email': data['email'], 'password': data['password']}

    # add the user to the list
    users.append(user)

    # return the user as a dictionary with status code 201 (created)
    return jsonify(user), 201

# define a route to get all users
@app.route('/users', methods=['GET'])
def get_users():
    # return the list of users as JSON
    return jsonify(users)

# define a route to get a specific user by ID
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    # loop through the list of users and find the user with the given ID
    for user in users:
        if user['id'] == user_id:
            # return the user as a dictionary
            return jsonify(user)

    # if the user does not exist, return an error dictionary with status code 404 (not found)
    return jsonify({'error': 'User not found'}), 404

# define a route to update a specific user by ID
@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    # loop through the list of users and find the user with the given ID
    for user in users:
        if user['id'] == user_id:
            # get the data from the request body
            data = request.get_json()

            # update the user dictionary with the new data
            user['name'] = data.get('name', user['name'])
            user['email'] = data.get('email', user['email'])
            user['password'] = data.get('password', user['password'])

            # return the updated user as a dictionary
            return jsonify(user)

    # if the user does not exist, return an error dictionary with status code 404 (not found)
    return jsonify({'error': 'User not found'}), 404

# define a route to delete a specific user by ID
@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    # loop through the list of users and find the user with the given ID
    for index, user in enumerate(users):
        if user['id'] == user_id:
            # delete the user from the list
            del users[index]

            # return an empty response with status code 204 (no content)
            return '', 204

    # if the user does not exist, return an error dictionary with status code 404 (not found)
    return jsonify({'error': 'User not found'}), 404

# run the app
if __name__ == '__main__':
    app.run(debug=True)
