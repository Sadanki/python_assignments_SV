import re

def check_password_strength(password):
    """
    Checks the strength of a given password based on the following criteria:
    - Minimum length of 8 characters.
    - Contains both uppercase and lowercase letters.
    - Contains at least one digit (0-9).
    - Contains at least one special character (e.g., !, @, #, $, %).
    Returns True if the password meets all criteria, otherwise False.
    """
    if len(password) < 8:
        return False

    # Define the regular expression patterns for each criterion
    patterns = {
        'lowercase letter': "[a-z]",
        'uppercase letter': "[A-Z]",
        'digit': "[0-9]",
        'special character': "[!@#$%^&*(),.?\":{}|<>]"
    }

    # Check each pattern to ensure the password meets the criteria
    for criterion, pattern in patterns.items():
        if not re.search(pattern, password):
            return False
    
    return True

def main():
    while True:
        user_password = input("Enter your password: ")

        if check_password_strength(user_password):
            print("Your password is strong.")
            break
        else:
            print("Your password is weak. Please ensure it meets the following criteria:")
            print("- At least 8 characters long")
            print("- Contains both uppercase and lowercase letters")
            print("- Contains at least one digit (0-9)")
            print("- Contains at least one special character (e.g., !, @, #, $, %)")
    
# Entry point for the script
if __name__ == "__main__":
    main()
