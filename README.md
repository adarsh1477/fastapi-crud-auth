# FastAPI CRUD with JWT Authentication

A production-ready FastAPI application featuring user authentication, blog post management, and secure API endpoints.

## Features

- **JWT Authentication**: Secure token-based auth with access tokens
- **OAuth2 Password Flow**: Industry-standard authentication pattern
- **CRUD Operations**: Complete blog post management (Create, Read, Update, Delete)
- **User Management**: User registration and profile management
- **Password Hashing**: Secure password storage with bcrypt
- **SQLite Database**: Lightweight database with SQLAlchemy ORM
- **Pydantic Validation**: Request/response validation and serialization

## Tech Stack

- **FastAPI**: Modern, fast web framework
- **SQLAlchemy**: SQL toolkit and ORM
- **Pydantic**: Data validation using Python type annotations
- **JWT**: JSON Web Tokens for authentication
- **Passlib**: Password hashing library
- **Uvicorn**: ASGI server

## API Endpoints

### Authentication
- `POST /user` - Register new user
- `POST /login` - Login and get JWT token

### Blog Posts
- `GET /blog` - Get all blog posts
- `GET /blog/{id}` - Get specific blog post
- `POST /blog` - Create new blog post (auth required)
- `PUT /blog/{id}` - Update blog post (auth required)
- `DELETE /blog/{id}` - Delete blog post (auth required)

### Users
- `GET /user/{id}` - Get user details

## Setup

1. Clone the repository
```bash
git clone https://github.com/adarsh1477/fastapi-crud-auth.git
cd fastapi-crud-auth
```

2. Install dependencies
```bash
pip install -r requirements.txt
```

3. Run the application
```bash
uvicorn main:app --reload
```

4. Access the API documentation at `http://localhost:8000/docs`

## Project Structure
```
fastapi-crud-auth/
├── blog/
│   ├── database.py      # Database configuration
│   ├── hashing.py       # Password hashing utilities
│   ├── models.py        # SQLAlchemy models
│   ├── oauth2.py        # JWT token handling
│   ├── schemas.py       # Pydantic schemas
│   └── token.py         # Token generation
├── routers/
│   ├── blog.py          # Blog endpoints
│   ├── user.py          # User endpoints
│   └── authentication.py # Auth endpoints
├── main.py              # Application entry point
├── requirements.txt     # Python dependencies
└── Dockerfile          # Docker configuration
```

## Authentication Flow

1. Register a user via `POST /user`
2. Login via `POST /login` to receive JWT access token
3. Include token in Authorization header: `Bearer <token>`
4. Access protected endpoints

## Development

Built as part of learning backend development with focus on:
- RESTful API design
- Authentication & authorization
- Database modeling & relationships
- API documentation
- Security best practices

## License

MIT
