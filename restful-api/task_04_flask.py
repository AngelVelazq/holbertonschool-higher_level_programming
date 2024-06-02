# Install Flask using pip: pip install Flask
from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory users dictionary
users = {
    "jane": {"username": "jane",
             "name": "Jane", "age": 28, "city": "Los Angeles"}
}


# Root endpoint
@app.route('/')
def home():
    return "Welcome to the Flask API!"


# /data endpoint to return all usernames
@app.route('/data')
def data():
    return jsonify(list(users.keys()))


# /status endpoint to return OK
@app.route('/status')
def status():
    return "OK"


# /users/<username> endpoint to return user details
@app.route('/users/<username>')
def get_user(username):
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404


# /add_user endpoint to add a new user
@app.route('/add_user', methods=['POST'])
def add_user():
    data = request.get_json()
    username = data.get('username')
    if not username or username in users:
        return jsonify({"error": "Invalid or existing username"}), 400
    users[username] = {
        "username": username,
        "name": data.get('name'),
        "age": data.get('age'),
        "city": data.get('city')
    }
    return jsonify({"message": "User added", "user": users[username]}), 201


# Run the Flask development server
if __name__ == "__main__":
    app.run(debug=True)
