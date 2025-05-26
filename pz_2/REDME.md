# Task for Pz 2

Design classes to manage user accounts with different levels of access to the system.

1. Create a base class `User` with the following attributes:
   - `username`: the name of the user;
   - `password_hash`: a hash of the user's password;
   - `is_active`: a boolean indicating whether the user account is active.

2. Implement a method `verify_password(password)` in the `User` class that receives a password and compares it to the `password_hash`.

3. Create subclasses that represent different user roles:
   - `Administrator`: inherits from `User` and includes additional attributes or methods related to system administration (e.g., a list of permissions).
   - `RegularUser`: inherits from `User` and includes attributes specific to regular users (e.g., last login date).
   - `GuestUser`: inherits from `User` and has limited access rights.

4. Create a class `AccessControl` with the following:
   - `users`: a dictionary where keys are usernames and values are user objects.
   - Method `add_user(user)`: adds a new user to the system.
   - Method `authenticate_user(username, password)`: checks if the user exists and if the password is correct. Returns the user object on success, or `None` on failure.


