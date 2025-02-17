# Flask User Management API

This is a simple **Flask-based REST API** for user management, storing user data in a JSON file. The project is **containerized using Docker** for easy deployment.

---
## Features
- Add a new user (`POST /users`)
- Get all users (`GET /users`)
- Get a specific user by ID (`GET /users/<id>`)
- Delete a user (`DELETE /users/<id>`)
- Uses a **JSON file** (`users.json`) as a lightweight database
- Docker support for easy deployment

---
## Installation & Setup

### 1️⃣ **Clone the Repository**
```sh
git clone https://github.com/YOUR_GITHUB_USERNAME/YOUR_REPO_NAME.git
cd YOUR_REPO_NAME
```

### 2️⃣ **Run the Flask App Locally**
Make sure you have Python installed.
```sh
pip install flask
python flask.py
```
The server will run on:  
📌 **http://127.0.0.1:5000/**

---
## Running with Docker

### 1️⃣ **Build the Docker Image**
```sh
docker build -t flask-user-api .
```

### 2️⃣ **Run the Docker Container**
```sh
docker run -p 8080:5000 flask-user-api
```
- The API will be available at:  
  📌 **http://127.0.0.1:8080/**

---
## API Endpoints

### ➤ **Add a User**
**POST** `/users`
```json
{
  "name": "John Doe",
  "email": "john@example.com"
}
```
_Response:_
```json
{
  "message": "User added successfully!",
  "user": {
    "id": 1,
    "name": "John Doe",
    "email": "john@example.com"
  }
}
```

### ➤ **Get All Users**
**GET** `/users`

### ➤ **Get a User by ID**
**GET** `/users/1`

### ➤ **Delete a User**
**DELETE** `/users/1`
_Response:_
```json
{
  "message": "User deleted successfully!"
}
```

