from flask import Flask, jsonify, request
import json

app = Flask(__name__)  # Create a Flask app

DATA_FILE = "users.json"  # JSON file to store users

# Function to load users from file
def load_users():
    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)  # Read from JSON file
    except (FileNotFoundError, json.JSONDecodeError):
        return []  # Return empty list if file doesn't exist or is empty

# Function to save users to file
def save_users(users):
    with open(DATA_FILE, "w") as file:
        json.dump(users, file, indent=4)  # Write users to JSON file

users = load_users()  # Load users when the app starts
user_id = max([user["id"] for user in users], default=0) + 1  # Get last user ID

# Home route
@app.route('/')
def home():
    return "<h1>Welcome to the Flask App with a Python List as Database!</h1>"

#Route to add user
@app.route('/users', methods=['POST'])
def add_user():
    global user_id
    data = request.json

    new_user = {
        "id": user_id,
        "name": data['name'],
        "email": data['email']
    }

    users.append(new_user)
    save_users(users)  # Save updated users to file
    user_id += 1  # Increment ID for next user

    return jsonify({"message": "User added successfully!", "user": new_user})

# Route to get all users
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)

#Route to get a specific user by ID
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    for user in users:
        if user["id"] == user_id:
            return jsonify(user)
    return jsonify({"error": "User not found"}), 404

# Route to delete a user by ID
@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    global users
    users = [user for user in users if user["id"] != user_id]
    return jsonify({"message": "User deleted successfully!"})

# if __name__ == '__main__':
#     app.run(debug=True)  # Runs on http://127.0.0.1:5000

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)