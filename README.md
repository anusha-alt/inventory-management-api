# Inventory Management API

This is a simple backend application to manage inventory for a small business. It exposes REST APIs to manage users and products using FastAPI and SQLite.

---

## Features

- User registration and JWT login
- Add new products
- Update product quantity
- View all products with pagination
- Swagger/OpenAPI documentation

---

## 🔧 Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/<your-username>/inventory-mangement-api.git
cd inventory-mangement-api
```
### 2. Set up a virtual environment
-On macOS/Linux: 
python3 -m venv venv
source venv/bin/activate

-On Windows:
python -m venv venv
venv\Scripts\activate

### 3. Install dependencies
pip install -r requirements.txt

### 4. Run the server
- uvicorn app.main:app --reload
- the server will run at: http://127.0.0.1:8000

### 5. API documentation
-Once the server is running, open your browser and visit: http://127.0.0.1:8000/docs. This opens the Swagger UI, where you can:

-Register a user

-Log in to receive a JWT token

-Authorize requests using the token

-Add, update, and fetch products

### 6. Project structure:
inventory-mangement-api/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── models.py
│   ├── schemas.py
│   ├── auth.py
│   └── routes.py
├── requirements.txt
├── README.md
└── Dockerfile (optional)

### 7. Endpoints summary
| Method | Endpoint                  | Description                              |
| ------ | ------------------------- | ---------------------------------------- |
| POST   | `/register`               | Register a new user                      |
| POST   | `/login`                  | Log in and receive a JWT token           |
| POST   | `/products`               | Add a new product (requires token)       |
| PUT    | `/products/{id}/quantity` | Update product quantity (requires token) |
| GET    | `/products`               | Get all products (requires token)        |


## Made with ❤️ by Anusha Venkatramanan







