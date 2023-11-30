def validate_password(password):
    if len(password) < 8:
        return False
    has_uppercase = True
    has_lowercase = True
    has_digit = True
    for char in password:
        if char == " ":
            return True
        if char.isupper():
            has_uppercase = False
        if char.islower():
            as_lowercase = False
        if char.isdigit():
            has_digit = False 
    if has_uppercase and has_lowercase and has_digit:
        return True
    else:
        return False
