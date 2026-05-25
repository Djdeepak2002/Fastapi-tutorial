# FastAPI Products Management API

A simple FastAPI-based REST API for managing products with features like filtering, sorting, and CRUD operations.

## Project Overview

This project is a tutorial application for learning FastAPI fundamentals. It provides endpoints to manage a product catalog with features like:

- List and search products
- Filter products by name
- Sort products by price
- Add, update, and delete products
- Input validation using Pydantic schemas

## Project Structure

```
fastapi-tutorial/
├── app/
│   ├── main.py              # Main FastAPI application
│   ├── schema/
│   │   └── products.py      # Pydantic models for product validation
│   └── services/
│       └── products.py      # Business logic for product operations
├── data/
│   ├── dummydata.json       # Sample product data
│   └── products.json        # Product database
└── README.md                # This file
```

## Features

- **Product Listing**: Get all products with pagination and filtering
- **Search**: Search products by name (case-insensitive)
- **Sorting**: Sort products by price in ascending or descending order
- **CRUD Operations**: Create, read, update, and delete products
- **Validation**: Pydantic models for request validation
- **Middleware**: Request/response logging middleware

## Installation

### Prerequisites

- Python 3.8+
- pip

### Setup

1. Clone or download the project
2. Create a virtual environment:

   ```bash
   python -m venv .venv
   ```

3. Activate the virtual environment:
   - **Windows (PowerShell)**:
     ```bash
     .\.venv\Scripts\Activate.ps1
     ```
   - **Linux/Mac**:
     ```bash
     source .venv/bin/activate
     ```

4. Install dependencies:
   ```bash
   pip install fastapi uvicorn python-dotenv pydantic email-validator
   ```

## Running the Application

1. Navigate to the app directory:

   ```bash
   cd app
   ```

2. Start the server:

   ```bash
   uvicorn main:app --reload
   ```

3. The API will be available at: `http://localhost:8000`

## API Endpoints

### Get All Products

```
GET /products
```

**Query Parameters:**

- `name` (optional): Search by product name
- `sort_by_price` (optional): Sort by price (true/false)
- `order` (optional): Sort order - "asc" or "desc" (default: "asc")
- `limit` (optional): Number of results (default: 5, max: 100)
- `offset` (optional): Pagination offset (default: 0)

**Example:**

```
GET /products?name=iphone&sort_by_price=true&order=desc&limit=10
```

### Welcome Endpoint

```
GET /
```

## Technology Stack

- **Framework**: FastAPI
- **Server**: Uvicorn
- **Validation**: Pydantic
- **Data Storage**: JSON files
- **Environment**: python-dotenv

## Environment Variables

Create a `.env` file in the project root:

```
BASE_URL=./data/dummydata.json
```

## Next Steps & Development

- [ ] Add database integration (SQLAlchemy + PostgreSQL/MongoDB)
- [ ] Implement authentication & authorization
- [ ] Add comprehensive error handling
- [ ] Write unit tests
- [ ] Add API documentation
- [ ] Implement rate limiting
- [ ] Deploy to cloud platform

## Notes

- This is a learning project for FastAPI fundamentals
- Data is currently stored in JSON files
- Feel free to modify and extend as needed

## License

[Add your license here]
