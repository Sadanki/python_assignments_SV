import re

def check_password_strength(password):
    """
    Validates password strength based on security requirements
    
    Args:
        password: String to be checked
        
    Returns:
        bool: True if password meets all criteria, False otherwise
    """
    # First check length as it's the quickest operation
    if len(password) < 8:
        return False
        
    # Check for required character types
    has_lower = False
    has_upper = False
    has_digit = False
    has_special = False
    
    # Single pass through password to check all criteria
    special_chars = "!@#$%^&*(),.?\":{}|<>"
    
    for char in password:
        if char.islower():
            has_lower = True
        elif char.isupper():
            has_upper = True
        elif char.isdigit():
            has_digit = True
        elif char in special_chars:
            has_special = True
            
    # Return True only if all criteria are met
    return all([has_lower, has_upper, has_digit, has_special])

def main():
    # Main program loop
    while True:
        # Get password input from user
        password = input("Enter a password to check: ")
        
        # Check password strength
        if check_password_strength(password):
            print("Password meets security requirements!")
            break
        else:
            # Provide feedback for weak password
            print("\nPassword must contain:")
            print("- Minimum 8 characters")
            print("- At least one uppercase letter")
            print("- At least one lowercase letter")
            print("- At least one number")
            print("- At least one special character (!@#$%^&*(),.?\":{}|<>)")
            print()

if __name__ == "__main__":
    main()