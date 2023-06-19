
import re

def password_strength_checker(password):
    # Checking for the minimum length
    if len(password) < 8:
        return "Password is too short. It should be at least 8 characters long."

    # Checking for uppercase letter
    if not re.search("[A-Z]", password):
        return "Password should have at least one uppercase letter."

    # Checking for lowercase letter
    if not re.search("[a-z]", password):
        return "Password should have at least one lowercase letter."

    # Checking for digits
    if not re.search("[0-9]", password):
        return "Password should have at least one numeral."

    # Checking for special characters
    if not re.search("[_@$]", password):
        return "Password should have at least one of the symbols $@#."

    return "Strong Password"

def main():
    password = input("Enter your password: ")
    print(password_strength_checker(password))

if __name__ == "__main__":
    main()
