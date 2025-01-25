# File-sharing-application
believe you want to convert the README into a .md file (Markdown format). Here's the content ready for that:

markdown
Copy
Edit
# Flask API with JWT Authentication and File Upload/Download

This is a Flask-based API for user authentication and file management. The API supports user registration, login with JWT authentication, file uploads, and file downloads. Users can upload files of specific formats (`.pptx`, `.docx`, `.xlsx`) and securely access them with a token.

## Features

- **User Signup**: Register new users with a username and password.
- **User Login**: Authenticate users and issue a JWT token.
- **File Upload**: Upload files with `.pptx`, `.docx`, `.xlsx` extensions.
- **File Download**: Download files securely by filename.
- **List Files**: View a list of uploaded files.

## Technologies

- **Flask**: The web framework used for creating the API.
- **JWT (JSON Web Token)**: For secure user authentication.
- **Werkzeug**: For hashing passwords.

## Installation

### Prerequisites

- Python 3.x
- Flask
- `werkzeug` for password hashing
- `pyjwt` for JWT handling

### Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/flask-jwt-file-api.git
   cd flask-jwt-file-api
Set up a virtual environment:

bash
Copy
Edit
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install required dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Create an uploads/ folder for storing uploaded files:

bash
Copy
Edit
mkdir uploads
Run the Flask app:

bash
Copy
Edit
python app.py
The API will be available at http://localhost:5000.

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
  "url": "encrypted_url_for_username"
}
2. POST /login
Description: Log in to get a JWT token.
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
Request Body: Form data (file upload)
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
JWT Authentication: All endpoints, except for /signup and /login, require a valid JWT token in the Authorization header.
File Type Restriction: Only .pptx, .docx, and .xlsx files are allowed for upload to ensure security.
