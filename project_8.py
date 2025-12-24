print("<----Password generator----->")

import random
import string

def generate_password(length, use_special_char=True):
    """Password generator function.
    
    Args:
        length (int): Length of the password.
        use_special_char (bool): Whether to include special characters."""
    
    char = string.ascii_letters
    char +=string.digits

    if use_special_char:
        char += string.punctuation

    password = ""

    for i in range(length):
        password += random.choice(char)
    return password

def check_strength(password):
    """Check the length of the password."""
    strength = 0
    if len(password) < 8:
        strength = 0
    elif 8 <= len(password) < 12:
        strength +=1
    else:
        strength +=2
    
    if any(char.isdigit() for char in password):
        strength +=1
    
    if any(char.isupper() for char in password) and any(char.islower() for char in password):
        strength +=1
    
    if strength <=2:
        return "Weak"
    elif strength >=3 and strength <=5:
        return "Moderate"
    else:
        return "Strong"
    
# MAIN PROGRAM
print("🔐 PASSWORD GENERATOR 🔐\n")

length = int(input("Enter desired password length (8-20): "))
is_special = input("Include special characters? (y/n): ").lower()
use_special_char = (is_special=="y")

password = generate_password(length, use_special_char)
strength = check_strength(password)

print(f"\n🔑 Your password: {password}")
print(f"🛡️ Strength: {check_strength(password)}")