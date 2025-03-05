# Flask Docker Project

This project demonstrates how to containerize a Flask application using Docker. It is a simple **Flask-based REST API** that allows users to be added, retrieved, and managed within a containerized environment.

---
## Project Structure
- `flask.py` - The main Flask application.
- `requirements.txt` - Contains required dependencies.
- `Dockerfile` - Instructions to build the Docker image.
- `users.json` - A simple JSON file used as a lightweight database.

---
## Building and Running with Docker

### 1️⃣ **Build the Docker Image**
```sh
docker build -t flask-docker-app .
```

### 2️⃣ **Run the Docker Container**
```sh
docker run -p 1111:2222 flask-docker-app
```
- The **first 1111** is the port on the host machine.
- The **second 2222** is the port inside the container where the Flask app runs.
- The API will be available at:  
  📌 **http://127.0.0.1:1111/**

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

---
## Dockerfile
```dockerfile
FROM python:3.9
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
EXPOSE 2222
CMD ["python", "app.py"]
```

---
## Environment Variables
You can configure environment variables using a `.env` file.

---
## Contributing
Feel free to submit issues or pull requests.

---
## License
This project is licensed under the MIT License.

