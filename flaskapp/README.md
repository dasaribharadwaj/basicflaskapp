# Sort Numbers Flask App
This is a simple Flask app that accepts a list of numbers via a POST request and returns a sorted list of numbers. It uses a Docker container to run the app and can be deployed using Docker Compose.

## Prerequisites
Before running the app, you'll need to have the following installed:

- Docker
- Docker Compose

## Getting started
To get started, clone this repository to your local machine:
```
cd flaskapp
```

## Running the app
To run the app, use the following command:
```
docker-compose up
```

This will start the app container and expose it on port 8000. You can then make requests to the app using a tool like curl or a web client.

## Making requests
```
python3 client.py
```