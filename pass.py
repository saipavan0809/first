import random
import string

def generate_password(length=12):
    # Define character sets
    characters = string.ascii_letters + string.digits + string.punctuation
    # Generate password
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Example usage
password = generate_password(16)  # You can change the length as needed
print(f"Generated Password: {password}")
