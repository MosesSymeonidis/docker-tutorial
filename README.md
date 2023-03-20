# User API

This repository contains two versions of a User API server, as well as a SDK for the stateless version.

## Stateful Version

The `stateful_server.py` file contains the code for the stateful version of the User API server. This version stores user data in a local SQLite database.

To run the server, you can execute the following command:


`python stateful_server.py`



## Stateless Version

The `stateless_server.py` file contains the code for the stateless version of the User API server. This version does not store user data locally, but rather relies on an external database.

To run the server, you can execute the following command:


`python stateless_server.py`


## User's SDK

The `user_api.py` file contains a SDK for the User API server. This SDK provides a set of methods for interacting with the API, including creating, retrieving, updating, and deleting users.

To use the SDK, you can create an instance of the `UserAPI` class and call its methods. For example:

```python
from user_api import UserAPI

# Create a new instance of the SDK
api = UserAPI('http://localhost:5000')

# Create a new user
user_data = {
    'name': 'John Doe',
    'email': 'johndoe@example.com',
    'password': '1111'
}
new_user = api.create_user(user_data)
print(new_user)

# Get all users
users = api.get_all_users()
print(users)

# Update a user
user_id = 1
updated_data = {
    'name': 'Jane Doe',
    'email': 'janedoe@example.com'
}
updated_user = api.update_user(user_id, updated_data)
print(updated_user)

# Delete a user
user_id = 1
api.delete_user(user_id)
```


## Requirements

The `requirements.txt` file lists the required Python packages for running the servers and using the SDK. You can install these packages using the following command:

`pip install -r requirements.txt`