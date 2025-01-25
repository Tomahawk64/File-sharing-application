from flask import Flask, request, jsonify, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
import os
import jwt
import datetime
from functools import wraps

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['UPLOAD_FOLDER'] = 'uploads/'

# Ensure the upload directory exists
if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

# Mock database
users = {}
files = {}

# Token decorator
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('Authorization')
        if not token:
            return jsonify({'message': 'Token is missing!'}), 403
        try:
            data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
        except jwt.ExpiredSignatureError:
            return jsonify({'message': 'Token has expired!'}), 403
        except jwt.InvalidTokenError:
            return jsonify({'message': 'Token is invalid!'}), 403
        return f(*args, **kwargs)
    return decorated

# Routes

@app.route('/signup', methods=['POST'])
def signup():
    data = request.json
    username = data['username']
    password = generate_password_hash(data['password'], method='sha256')
    if username in users:
        return jsonify({'message': 'User already exists!'}), 400
    users[username] = {'password': password, 'role': 'client'}
    return jsonify({'message': 'User created!'}), 201

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data['username']
    password = data['password']
    user = users.get(username)
    if not user or not check_password_hash(user['password'], password):
        return jsonify({'message': 'Invalid credentials!'}), 401
    token = jwt.encode({'user': username, 'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)}, app.config['SECRET_KEY'])
    return jsonify({'token': token})

@app.route('/upload', methods=['POST'])
@token_required
def upload_file():
    file = request.files.get('file')
    if not file or not file.filename.endswith(('.pptx', '.docx', '.xlsx')):
        return jsonify({'message': 'Invalid file type!'}), 400
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(file_path)
    files[file.filename] = file.filename
    return jsonify({'message': 'File uploaded successfully!'}), 201

@app.route('/download-file/<filename>', methods=['GET'])
@token_required
def download_file(filename):
    if filename in files:
        return send_from_directory(app.config['UPLOAD_FOLDER'], filename, as_attachment=True)
    return jsonify({'message': 'File not found!'}), 404

@app.route('/list-files', methods=['GET'])
@token_required
def list_files():
    return jsonify({'files': list(files.keys())})

@app.route('/secure-download-link/<filename>', methods=['GET'])
@token_required
def generate_download_link(filename):
    if filename in files:
        token = jwt.encode({'filename': filename, 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=10)}, app.config['SECRET_KEY'])
        return jsonify({'download-link': f'/secure-download/{token}', 'message': 'success'})
    return jsonify({'message': 'File not found!'}), 404

@app.route('/secure-download/<token>', methods=['GET'])
def secure_download(token):
    try:
        payload = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
        filename = payload.get('filename')
        if filename and filename in files:
            return send_from_directory(app.config['UPLOAD_FOLDER'], filename, as_attachment=True)
        return jsonify({'message': 'File not found!'}), 404
    except jwt.ExpiredSignatureError:
        return jsonify({'message': 'Token has expired!'}), 403
    except jwt.InvalidTokenError:
        return jsonify({'message': 'Invalid token!'}), 403

if __name__ == '__main__':
    app.run(debug=True)
