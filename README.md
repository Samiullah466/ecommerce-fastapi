- Ecommerce API

A production-ready backend REST API for an ecommerce platform built with FastAPI.
The API provides secure authentication, product management, cart operations, order processing, and user profile management.

It follows **modern backend architecture**, **JWT authentication**, and automatic API documentation using Swagger UI.


- Features

1- Authentication

- User Signup
- User Login
- JWT Authentication
- Forgot Password
- Reset Password
- Password Strength Validation

2- Product Management

- Add Product
- List Products
- Update Product
- Delete Product

3- Cart System

- Add items to cart
- View cart
- Update item quantity
- Remove item from cart

4- Order System

- Create order
- View user orders

5- User Profile

- Get user profile
- Update profile
- Change password

6- Developer Tools

- Automatic API docs
- RESTful architecture
- API testing with Postman


7- Tech Stack

| Technology          | Purpose              |
| ------------------- | -------------------- |
| Python              | Programming language |
| FastAPI             | Backend framework    |
| SQLAlchemy          | ORM                  |
| SQLite / PostgreSQL | Database             |
| JWT                 | Authentication       |
| Migrations	      | Alembic
| Uvicorn             | ASGI server          |
| Postman             | API testing          |


8- Project Structure

Ecommerce_API
│
├── app
│   ├── api
│   │   └── routes
│   │       ├── auth_routes.py
│   │       ├── product_routes.py
│   │       ├── cart_routes.py
│   │       ├── order_routes.py
│   │       └── user_routes.py
│   │
│   ├── models
│   │   ├── user.py
│   │   ├── product.py
│   │   ├── cart.py
│   │   └── order.py
│   │
│   ├── schemas
│   │   ├── user_schema.py
│   │   ├── product_schema.py
│   │   ├── cart_schema.py
│   │   └── order_schema.py
│   │
│   ├── services
│   │   ├── auth_service.py
│   │   ├── product_service.py
│   │   ├── cart_service.py
│   │   └── order_service.py
│   │
│   ├── utils
│   │   ├── security.py
│   │   └── password_validator.py
│   │
│   └── main.py
│
├── requirements.txt
└── README.md


9- Installation

-> Clone the repository
- git clone https://github.com/Samiullah466/ecommerce-fastapi.git
- cd ecommerce-api


-> Create virtual environment
- python -m venv venv

-> Activate virtual environment

-> Windows
- venv\Scripts\activate


-> Install dependencies
- pip install -r requirements.txt

-> Setup environment variables

- Create a .env file:

DATABASE_URL=your_database_url
SECRET_KEY=your_secret_key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30

-> Database Migration
- alembic upgrade head

-> Run the server
- uvicorn app.main:app --reload


-> Server will run on
- http://127.0.0.1:8000


10- API Documentation
->Interactive API docs available at
- http://127.0.0.1:8000/docs

-> OpenAPI schema
- /openapi.json

11- Authentication
-> The API uses **JWT tokens** for authentication.
-> Example login request
- POST /auth/login

-> Example response

```json
{
 "access_token": "JWT_TOKEN",
 "token_type": "bearer"
}
```

-> Use the token in headers
- Authorization: Bearer JWT_TOKEN


12- Password Reset Flow

12.1- Forgot Password

- POST /auth/forgot-password

-> Generates a reset token.

12.2- Reset Password

- POST /auth/reset-password

-> Request

```json
{
 "token": "RESET_TOKEN",
 "new_password": "NewStrongPassword123!"
}
```


13- API Endpoints

13.1- Auth

POST /auth/signup
POST /auth/login
POST /auth/forgot-password
POST /auth/reset-password


13.2- Products

POST /products/
GET /products/
PUT /products/{product_id}
DELETE /products/{product_id}


13.3- Cart

POST /cart/
GET /cart/
PATCH /cart/{item_id}/quantity
DELETE /cart/{item_id}

13.4- Orders

POST /orders/
GET /orders/my-orders

13.4- User

GET /profile/
PUT /profile/
PUT /profile/change-password

14- Testing

API testing was performed using **Postman** with a structured collection including:

- Authentication tests
- Product CRUD tests
- Cart functionality tests
- Order processing tests
- Profile management tests


15- Security

- Password hashing
- JWT authentication
- Password strength validation
- Secure password reset tokens
- Protected routes


16- Future Improvements

- Email-based password reset
- Payment integration (Stripe)
- Product image upload
- Admin dashboard
- Docker deployment
- CI/CD pipeline


17- Author

**Sami Ullah**

Backend Developer
FastAPI | Python | REST APIs


-> If you like this project, consider giving it a **star on GitHub**.

