#  Write a Python program to check the validity of passwords input by users.
# At least 1 letter between [a-z] and 1 letter between [A-Z].
# At least 1 number between [0-9].
# At least 1 character from [$#@].
# Minimum length 6 characters.
# Maximum length 16 characters.

password = "ijKL@26"
chars = "$#@"

def check_digit(password):
    """Check if password contains at least 1 number from [0-9]."""
    return any(i.isdigit() for i in password)

def check_lower(password):
    """Check if password contains at least 1 letter between [a-z]."""
    return any(i.islower() for i in password)

def check_upper(password):
    """Check if password contains at least 1 letter between [A-Z]."""
    return any(i.isupper() for i in password)

def check_special(password, chars):
    """Check if password contains at least 1 character [$@#]."""
    return any(i in chars for i in password)


while True:
    if len(password) < 6:
        print("Error: Minimum length 6 characters!!!")
        break
    elif len(password) > 16:
        print("Error: Maximum length 16 characters!!!")
        break

    elif not check_digit(password):
        print("Should contain at least 1 number between [0-9]!!")
        break

    elif not check_lower(password):
        print("Should contain at least 1 letter between [a-z]!!")
        break

    elif not check_lower(password):
        print("Should contain at least 1 letter between [a-z]!!")
        break

    elif not check_special(password, chars):
        print("Should contain at least 1 character from [$#@]!!")
        break
    else:
        print("Password is valid.")
    break






