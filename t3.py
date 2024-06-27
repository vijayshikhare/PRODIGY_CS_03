import re

def assess_password_strength(password):
    # Initialize strength level and feedback messages
    strength = 0
    feedback = []
    
    # Check length
    if len(password) >= 8:
        strength += 1
    else:
        feedback.append("Password should be at least 8 characters long.")
    
    # Check for uppercase letters
    if re.search(r'[A-Z]', password):
        strength += 1
    else:
        feedback.append("Password should contain at least one uppercase letter.")
    
    # Check for lowercase letters
    if re.search(r'[a-z]', password):
        strength += 1
    else:
        feedback.append("Password should contain at least one lowercase letter.")
    
    # Check for numbers
    if re.search(r'\d', password):
        strength += 1
    else:
        feedback.append("Password should contain at least one number.")
    
    # Check for special characters
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        strength += 1
    else:
        feedback.append("Password should contain at least one special character.")
    
    # Determine password strength level
    if strength == 5:
        feedback.append("Password strength: Very Strong")
    elif strength == 4:
        feedback.append("Password strength: Strong")
    elif strength == 3:
        feedback.append("Password strength: Moderate")
    elif strength == 2:
        feedback.append("Password strength: Weak")
    else:
        feedback.append("Password strength: Very Weak")
    
    return feedback

# Example usage
password = "Vijay@4545"
feedback = assess_password_strength(password)
for message in feedback:
    print(message)
