from user_api import UserAPI

api = UserAPI('http://localhost:5000')

user_data = {
    'name': 'John Doe',
    'email': 'johndoe@example.com',
    'password': '1111'
}

new_user = api.create_user(user_data)

print(new_user)