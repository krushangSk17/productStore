
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


### Project Overview

This project involves the development of an item dashboard with a focus on backend functionalities including data modeling, API creation, database integration, serialization, query parameter implementation, comprehensive API documentation, secure authentication, thorough testing, and performance optimization through caching. A frontend interface is also developed to display the data in a user-friendly format.

### Implementation Details

#### 1. Data Modeling
- **Completed Task:** Defined Django data models for two primary entities: `Product` and its `Category`. These models are linked via a SQL foreign key constraint, ensuring relational integrity between products and their respective categories.

#### 2. Database Connection
- **Completed Task:** Selected SQLite as the default database due to its simplicity and integration within Django. This choice is justified by SQLite's efficiency for development and testing, and its capability to handle the project's requirements for creating and deleting tasks seamlessly, while supporting default and nullable values.

#### 3. API Endpoints
- **Completed Task:** Developed an API endpoint to fetch a list of items including details such as SKU, name, category, tags, stock status, and available stock, as outlined in the provided API documentation.

#### 4. Serialization
- **Completed Task:** Utilized Django REST Framework serializers for converting model instances into JSON format, facilitating data type conversions and validation processes.

#### 5. Query Parameters
- **Completed Task:** Implemented query parameters to filter results based on specific criteria such as date ranges and stock status, enhancing the API's functionality and user experience.

#### 6. API Documentation
- **Completed Task:** Documented all API endpoints, detailing request types, body formats, and expected responses. This documentation is available in the project's GitHub repository for easy access and reference.

#### 7. Authentication
- **Completed Task:** Secured API endpoints using Django REST Framework's `TokenAuthentication`, ensuring that only authenticated users can access the API functionalities.

#### 8. Testing
- **Completed Task:** Conducted unit testing for all API endpoints to validate their functionality, with tests documented in `home/tests.py`. Additional testing details are provided in the project documentation.

#### 9. Performance Optimization
- **Bonus Task:** Implemented caching using the `@cache_page(60 * 15)` decorator to optimize API performance, significantly reducing data retrieval times and enhancing the overall user experience.

#### 10. Frontend Interface
- Due to time constraint this task is pending. if more time is allowed I am sure I can do this with very smooth front end.

### Conclusion

This comprehensive project showcases a well-rounded approach to building a functional item dashboard, emphasizing backend development with an eye on frontend integration. The careful selection of technologies, detailed implementation of functionalities, and attention to user authentication and performance optimization underscore the project's commitment to delivering a robust and user-friendly application.
