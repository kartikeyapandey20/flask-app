User Management API Documentation
This document outlines the functionalities and endpoints of the User Management API built using Flask and MySQL.

Endpoints
1. GET /user/getall
Description: Retrieve all users.
Method: GET
Response: Returns a list of all users in the database.
2. POST /user/addone
Description: Add a single user.
Method: POST
Request Body: JSON data containing user details (name, email, phone, role, password).
Response: Returns a success message upon successful user creation.
3. POST /user/addmultiple
Description: Add multiple users in bulk.
Method: POST
Request Body: JSON array containing multiple user details (name, email, phone, role, password).
Response: Returns a success message upon successful creation of multiple users.
4. PUT /user/updateone
Description: Update details of a single user.
Method: PUT
Request Body: JSON data containing updated user details (name, email, phone, role, password).
Response: Returns a success message upon successful user update.
5. DELETE /user/delete/<id>
Description: Delete a user by ID.
Method: DELETE
Parameters: id (User ID)
Response: Returns a success message upon successful deletion of the user.
6. PATCH /user/patch/<id>
Description: Update specific details of a user.
Method: PATCH
Parameters: id (User ID)
Request Body: JSON data containing specific fields to update.
Response: Returns a success message upon successful partial user update.
7. GET /user/limit/<limit>/page/<page>
Description: Paginated retrieval of users.
Method: GET
Parameters: limit (Number of users per page), page (Page number)
Response: Returns paginated user data with page number and limit.
8. PUT /user/<uid>/upload/avatar
Description: Upload avatar for a user.
Method: PUT
Parameters: uid (User ID)
Request: Form data with the 'avatar' file.
Response: Returns a success message upon successful avatar upload for the user.
9. GET /uploads/<filename>
Description: Retrieve uploaded avatar by filename.
Method: GET
Parameters: filename (Avatar file name)
Response: Returns the requested avatar file.
10. POST /user/login
Description: User login authentication.
Method: POST
Request Body: JSON data containing user email and password.
Response: Returns a JWT token upon successful login.
Authentication
Token-based authentication is implemented for certain endpoints using a JWT (JSON Web Token) approach.

Token Generation
The /user/login endpoint generates a JWT token upon successful user authentication.
Token Authentication
Endpoints annotated with @auth.token_auth() utilize token-based authentication.
The token is passed in the Authorization header as Bearer <token> for access.
The token is verified and decoded to authenticate and authorize user access to protected endpoints based on role permissions.
Models Used
1. UserModel
Handles user-related database operations.
Methods include user retrieval, addition, update, deletion, pagination, avatar upload, and login functionality.
2. TokenModel
Manages token-based authentication for endpoints.
Validates JWT tokens and authorizes access based on user roles and endpoint permissions.
This documentation provides an overview of the User Management API, its functionalities, endpoints, authentication methods, and the models used for data operations.