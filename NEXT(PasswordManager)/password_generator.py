import random
import string

def create_password():
    password = []

    for _ in range(1):
        password.append(random.choice(string.ascii_uppercase))
    
    for _ in range(2):
        password.append(random.choice(string.ascii_lowercase))

    for _ in range(3):
        password.append(random.choice(string.digits))

    for _ in range(3):
        password.append(random.choice(string.ascii_lowercase))
    
    for _ in range(1):
        password.append(random.choice("!@#$%&?"))
        
    return "".join(password)

    