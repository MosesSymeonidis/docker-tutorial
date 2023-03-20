import requests


class UserAPI:
    def __init__(self, base_url):
        self.base_url = base_url  # The base URL of the User API

    def create_user(self, data):
        # Sends a POST request to create a new user using the provided data
        # Raises an exception if the request fails
        response = requests.post(f'{self.base_url}/users', json=data)
        response.raise_for_status()

        # Returns the JSON response from the API call
        return response.json()

    def get_all_users(self):
        # Sends a GET request to retrieve all users
        # Raises an exception if the request fails
        response = requests.get(f'{self.base_url}/users')
        response.raise_for_status()

        # Returns the JSON response from the API call
        return response.json()

    def get_user(self, user_id):
        # Sends a GET request to retrieve a specific user by ID
        # Raises an exception if the request fails
        response = requests.get(f'{self.base_url}/users/{user_id}')
        response.raise_for_status()

        # Returns the JSON response from the API call
        return response.json()

    def update_user(self, user_id, data):
        # Sends a PUT request to update a specific user by ID with the provided data
        # Raises an exception if the request fails
        response = requests.put(f'{self.base_url}/users/{user_id}', json=data)
        response.raise_for_status()

        # Returns the JSON response from the API call
        return response.json()

    def delete_user(self, user_id):
        # Sends a DELETE request to delete a specific user by ID
        # Raises an exception if the request fails
        response = requests.delete(f'{self.base_url}/users/{user_id}')
        response.raise_for_status()
