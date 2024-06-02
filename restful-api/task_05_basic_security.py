from flask import Flask, jsonify, request
from werkzeug.security import generate_password_hash, \
    check_password_hash
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import JWTManager, create_access_token, \
    jwt_required, get_jwt_identity

app = Flask(__name__)
auth = HTTPBasicAuth()

# Secret key for JWT
app.config['JWT_SECRET_KEY'] = 'your_jwt_secret_key'  # Change this
jwt = JWTManager(app)

# In-memory users dictionary with hashed passwords
users = {
    "john": generate_password_hash("password123"),
    "jane": generate_password_hash("password456")
}

# User roles
user_roles = {
    "john": "admin",
    "jane": "user"
}

# Basic Auth verification
@auth.verify_password
def verify_password(username, password):
    if username in users and check_password_hash(users.get(username),
                                                 password):
        return username
    return None

# Root endpoint
@app.route('/')
def home():
    return "Welcome to the Flask API!"

# Protected /basic-protected endpoint with Basic Auth
@app.route('/basic-protected')
@auth.login_required
def basic_protected():
    return "Basic Auth: Access Granted"

# JWT login route
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    if username in users and check_password_hash(users.get(username),
                                                 password):
        access_token = create_access_token(identity={'username': username,
                                                     'role': user_roles.get(
                                                         username)})
        return jsonify(access_token=access_token), 200
    return jsonify({"error": "Invalid credentials"}), 401

# Protected /jwt-protected route with JWT
@app.route('/jwt-protected', methods=['GET'])
@jwt_required()
def jwt_protected():
    return "JWT Auth: Access Granted"

# Role-based access control decorator
def role_required(role):
    def decorator(f):
        @jwt_required()
        def wrapped(*args, **kwargs):
            current_user = get_jwt_identity()
            if current_user['role'] != role:
                return jsonify({"error": "Access forbidden: Requires {} role"
                                .format(role)}), 403
            return f(*args, **kwargs)
        return wrapped
    return decorator

# /admin-only endpoint accessible only by admin users
@app.route('/admin-only')
@role_required('admin')
def admin_only():
    return "Admin Access: Granted"

# Run the Flask development server
if __name__ == "__main__":
    app.run(debug=True)
