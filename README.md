# Blog API with JWT Authentication

A REST API built with FastAPI and SQLAlchemy featuring 
secure JWT authentication.

## Features
- User registration with password hashing
- JWT token authentication
- Protected routes
- Blog post CRUD operations
- One-to-Many relationships

## Tech Stack
- Python
- FastAPI
- SQLAlchemy
- SQLite
- JWT (python-jose)
- bcrypt (passlib)

## Endpoints
- POST /register
- POST /login
- GET /posts
- POST /posts 🔒
- GET /posts/{id}
- PUT /posts/{id} 🔒
- DELETE /posts/{id} 🔒
