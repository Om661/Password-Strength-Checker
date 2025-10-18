import re

def check_password_strength(password):
    strength = 0
    remarks = ""
    
    if len(password) < 6:
        remarks = "Password too short. Minimum 6 characters."
    elif len(password) >= 8:
        strength += 1
    
    if re.search("[a-z]", password):
        strength += 1
    if re.search("[A-Z]", password):
        strength += 1
    if re.search("[0-9]", password):
        strength += 1
    if re.search("[@#$%^&+=!]", password):
        strength += 1
    
    if strength <= 2:
        remarks = "Weak password. Try adding numbers, uppercase, and symbols."
    elif strength == 3:
        remarks = "Moderate password. Add more variety."
    else:
        remarks = "Strong password!"
    
    return strength, remarks

# Run the program
if __name__ == "__main__":
    pwd = input("Enter your password: ")
    strength, msg = check_password_strength(pwd)
    print(f"\nStrength Score: {strength}/5")
    print(f"Feedback: {msg}")
