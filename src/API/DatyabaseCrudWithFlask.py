from flask import Flask, request, jsonify, render_template
from services import UserService  # assuming services.py contains all your service classes

app = Flask(__name__, template_folder='Front')

@app.route('/map')
def map():
    return render_template('map.html')

@app.route('/user', methods=['POST'])
def create_user():
    username = request.json.get('username')
    password = request.json.get('password')
    UserService().create_user(username, password)
    return jsonify({'message': 'User created successfully'}), 201

@app.route('/user/<user_id>', methods=['GET'])
def get_user(user_id):
    user = UserService().get_user(user_id)
    if user:
        return jsonify({'username': user.Str_UserName}), 200
    else:
        return jsonify({'error': 'User not found'}), 404

@app.route('/user/<user_id>', methods=['PUT'])
def update_user(user_id):
    username = request.json.get('username')
    password = request.json.get('password')
    UserService().update_user(user_id, username, password)
    return jsonify({'message': 'User updated successfully'}), 200

@app.route('/user/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    UserService().delete_user(user_id)
    return jsonify({'message': 'User deleted successfully'}), 200

if __name__ == '__main__':
    app.run(debug=True)
