def validate_password(password, password_confirm):
    if password != password_confirm:
        return "Passwords do not match"
    if len(password) < 8:
        return "Password must be at least 8 characters long"
    if not any(char.isdigit() for char in password):
        return "Password must contain at least one number"
    if not any(char.isupper() for char in password):
        return "Password must contain at least one uppercase letter"
    return None
