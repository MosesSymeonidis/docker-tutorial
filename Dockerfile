# Use an official Python runtime as a parent image
# TODO create a dockerfile with python:3.8-slim-buster as base image

# TODO Set the working directory to /app

# TODO Copy the requirements file into the container and install dependencies
# tip: the dependences will be installed by executing pip install --no-cache-dir -r requirements.txt


# Copy the server files into the container
#COPY stateful_server.py .
#COPY stateless_server.py .
#COPY user_api.py .

# TODO Expose the port 5000

# Define environment variables
#ENV FLASK_APP stateful_server.py
#ENV FLASK_ENV production

# Run the stateful server by default
# TODO write a command for flask run --host:0.0.0.0