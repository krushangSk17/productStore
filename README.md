
# API Documentation

## Overview

This documentation provides detailed information on the API endpoints available for managing products, categories, user authentication, registration, and password management. These endpoints allow for the retrieval, creation, and modification of product and category data, as well as user management on the platform.

## Base URL

All API requests should be made to the base URL:
```
https://krushang17.pythonanywhere.com/api/
```

## Authentication

Several endpoints require authentication. This is achieved by obtaining a token through the `/api-token-auth/` endpoint and including it in the request headers as follows:
```
Authorization: Token <your_token_here>
```

### Obtaining a Token

- **POST** `https://krushang17.pythonanywhere.com/api/api-token-auth/`

  **Body:**
  ```json
  {
    "username": "krushang",
    "password": "krushangsatani"
  }
  ```

  **Response:**
  ```json
  {
    "token": "684b207b0257d73747bcfd0e58ca09fa05ff4aec"
  }
  ```

## Endpoints

### User Management

#### New User Registration

- **POST** `https://krushang17.pythonanywhere.com/api/register/`

  **Body:**
  ```json
  {
    "username": "un1",
    "password": "un1",
    "email": "un1@g.com"
  }
  ```

  **Description:** Allows for the registration of a new user without requiring authentication.

#### Change Password

- **POST** `https://krushang17.pythonanywhere.com/api/change-password/`

  **Body:**
  ```json
  {
    "username": "the_username",
    "newpassword": "the_new_password"
  }
  ```

  **Description:** Allows users to change their password without authentication.

### Product Management

#### Get Products and Category

- **GET** `https://krushang17.pythonanywhere.com/api/get-products/`

  **Headers:**
  ```
  Authorization: Token 684b207b0257d73747bcfd0e58ca09fa05ff4aec
  ```

  **Parameters:**
  - `start_date`: Filter products created on or after this date.
  - `end_date`: Filter products created on or before this date.

  **Example Request:**
  ```
  /get-products/?start_date=2022-01-01T00:00:00&end_date=2025-01-31T23:59:59
  ```

### Category Management

#### Add Category

- **POST** `https://krushang17.pythonanywhere.com/api/save-category/`

  **Headers:**
  ```
  Authorization: Token <your_token_here>
  ```

  **Body:**
  ```json
  {
    "name": "cat2"
  }
  ```

  **Description:** Adds a new category to the system. Requires authentication.


#### Add Product

- **POST** `https://krushang17.pythonanywhere.com/api/save-product/`

  **Headers:**
  ```
  Authorization: Token <your_token_here>
  ```

  **Body:**
  ```json
  {
    "sku": "ABC",
    "name": "abc product",
    "category": "cat2",
    "tags": ["a", "b", "c"],
    "stock_status": 100,
    "available_stock": 50
  }
  ```

  **Description:** Adds a new product to the system. Requires authentication.

### Delete Product

- **POST** (`https://krushang17.pythonanywhere.com/api/delete-product/`)

  **Body:**
  ```json
  {
    "id": "1"
  }
  ```

  **Description:** Deletes a product by ID. Specifics about authentication and the exact endpoint were not provided.

## Examples

### Adding a Product

1. **Obtain an authentication token** as described in the Obtaining a Token section.
2. **Add a category** (if necessary) by using the `/save-category/` endpoint.
3. **Add a product** by using the `/save-product/` endpoint with the token obtained in step 1.

This process ensures that the products are categorized correctly and that all interactions with the API are secure.

---

This documentation format provides a clear and concise overview of each endpoint, including necessary authentication steps and detailed examples for critical operations. It's designed to help developers quickly understand and integrate with your API.
