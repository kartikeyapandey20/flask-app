# User Management API

This API is designed to manage user-related operations using Flask and MySQL.

## Endpoints

### 1. GET /user/getall
Retrieve all users.

### 2. POST /user/addone
Add a single user.

### 3. POST /user/addmultiple
Add multiple users in bulk.

### 4. PUT /user/updateone
Update details of a single user.

### 5. DELETE /user/delete/<id>
Delete a user by ID.

### 6. PATCH /user/patch/<id>
Update specific details of a user.

### 7. GET /user/limit/<limit>/page/<page>
Paginated retrieval of users.

### 8. PUT /user/<uid>/upload/avatar
Upload avatar for a user.

### 9. GET /uploads/<filename>
Retrieve uploaded avatar by filename.

### 10. POST /user/login
User login authentication.

## Authentication

Token-based authentication is implemented for certain endpoints using a JWT (JSON Web Token) approach.

### Token Generation
- The `/user/login` endpoint generates a JWT token upon successful user authentication.

### Token Authentication
- Endpoints annotated with `@auth.token_auth()` utilize token-based authentication.
- The token is passed in the `Authorization` header as `Bearer <token>` for access.
- The token is verified and decoded to authenticate and authorize user access to protected endpoints based on role permissions.

## Models Used

### 1. `UserModel`
- Handles user-related database operations.
- Methods include user retrieval, addition, update, deletion, pagination, avatar upload, and login functionality.

### 2. `TokenModel`
- Manages token-based authentication for endpoints.
- Validates JWT tokens and authorizes access based on user roles and endpoint permissions.

## Installation

1. Clone the repository.
2. Install the required dependencies using `pip install -r requirements.txt`.
3. Configure the MySQL database connection in `config/config.py`.

## Usage

1. Run the Flask application using `python app.py`.
2. Access the API endpoints using a tool like Postman or any HTTP client.

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.

## License

This project is licensed under the [MIT License](LICENSE).
