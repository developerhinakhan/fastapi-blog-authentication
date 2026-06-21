# Blog API with JWT Authentication

A REST API built with FastAPI and SQLAlchemy featuring secure JWT authentication.

## Features

- User registration with password hashing
- JWT token authentication
- Protected routes
- Blog post CRUD operations
- One-to-Many relationships (users to posts)

## Tech Stack

- Python
- FastAPI
- SQLAlchemy
- SQLite
- JWT (python-jose)
- bcrypt (passlib)

## Installation

**1. Clone the repository**
```bash
git clone https://github.com/developerhinakhan/fastapi-blog-authentication.git
cd fastapi-blog-authentication
```

**2. Create virtual environment**
```bash
python -m venv myenv
source myenv/Scripts/activate
```

**3. Install dependencies**
```bash
pip install -r requirements.txt
```

**4. Set up environment variables**
```bash
cp .env.example .env
```
Then open `.env` and set your own `SECRET_KEY`.

**5. Run the server**
```bash
uvicorn main:app --reload
```

**6. Open Swagger UI**
http://127.0.0.1:8000/docs

## API Endpoints

- `POST /register` — Register a new user
- `POST /login` — Log in and receive a JWT access token
- `GET /posts` — List all posts
- `POST /posts` 🔒 — Create a new post
- `GET /posts/{id}` — Get a single post
- `PUT /posts/{id}` 🔒 — Update a post (owner only)
- `DELETE /posts/{id}` 🔒 — Delete a post (owner only)

🔒 = requires authentication (Bearer token)

## Developer

**Hina Noor**
Python Backend Developer
GitHub: [developerhinakhan](https://github.com/developerhinakhan)
