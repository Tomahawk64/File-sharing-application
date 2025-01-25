# File-sharing-application
Flask API with JWT Authentication and File Upload/Download
This repository contains a simple Flask API with JWT authentication, file upload, and file download functionalities. It is designed to handle user registration, login, and secure file handling for specified file types (.pptx, .docx, .xlsx).

Features
User Signup: Allows users to sign up with a username and password.
User Login: Allows users to log in using their credentials, and get a JWT token.
File Upload: Allows authenticated users to upload files (only .pptx, .docx, .xlsx).
File Download: Allows authenticated users to download files by filename.
List Files: Allows authenticated users to see a list of uploaded files.
Technologies Used
Flask: Web framework for creating the API.
JWT: JSON Web Tokens for secure authentication.
Werkzeug: Used for password hashing.
Python: The primary programming language for the backend.
Installation
Prerequisites
Python 3.x
Flask
werkzeug for password hashing
pyjwt for JWT handling
Setup
Clone this repository:

bash
Copy
Edit
git clone https://github.com/yourusername/flask-jwt-file-api.git
cd flask-jwt-file-api
Create a virtual environment (optional but recommended):

bash
Copy
Edit
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install the required dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Create an uploads/ directory in the project root to store uploaded files:

bash
Copy
Edit
mkdir uploads
Run the Flask app:

bash
Copy
Edit
python app.py
The API will now be running at http://localhost:5000.

API Endpoints

1. POST /signup
Description: Create a new user.
Request Body:
json
Copy
Edit
{
  "username": "your_username",
  "password": "your_password"
}
Response:
json
Copy
Edit
{
  "message": "User created!",
  "url": "encrypted_url_for_your_username"
}

2. POST /login
Description: Log in with username and password to get a JWT token.
Request Body:
json
Copy
Edit
{
  "username": "your_username",
  "password": "your_password"
}
Response:
json
Copy
Edit
{
  "token": "your_jwt_token"
}

3. POST /upload
Description: Upload a file (only .pptx, .docx, .xlsx).
Headers:
Authorization: Bearer <JWT_TOKEN>
Body: Form data (file upload)
Response:
json
Copy
Edit
{
  "message": "File uploaded successfully!"
}

4. GET /download-file/{filename}
Description: Download a file.
Headers:
Authorization: Bearer <JWT_TOKEN>
Response:
json
Copy
Edit
{
  "download-link": "/download-file/{filename}",
  "message": "success"
}

5. GET /list-files
Description: List all uploaded files.
Headers:
Authorization: Bearer <JWT_TOKEN>
Response:
json
Copy
Edit
{
  "files": ["file1.pptx", "file2.docx"]
}

Security
The API uses JWT for authentication. Ensure you keep the SECRET_KEY safe in production.
File uploads are restricted to .pptx, .docx, and .xlsx formats to prevent malicious files from being uploaded.


Contribution
Feel free to fork the repository and make improvements. If you find a bug or have a feature request, please open an issue.
