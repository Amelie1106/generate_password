import os
import hashlib
import random
def generate_password():
    lowercase = 'abcdefghijklmnopqrstuvwxyz'
    uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    numbers = '0123456789'
    special_chars = '!@#$%&*'
    all_chars = lowercase + uppercase + numbers + special_chars
    # Random length between 8 and 16
    length = random.randint(8, 16)
    password = []
    # Ensure at least one character from each required set
    password.append(random.choice(lowercase))
    password.append(random.choice(uppercase))
    password.append(random.choice(numbers))
    password.append(random.choice(special_chars))
    # Fill the rest of the password
    for _ in range(len(password), length):
        password.append(random.choice(all_chars))
    # Shuffle the password list and join to form the final string
    random.shuffle(password)
    final_password = ''.join(password)
    return final_password
password = generate_password()
print('the password: ' + password)
def get_hashed_password(password):
    salt = os.urandom(8).hex()
    hashed_password = hashlib.scrypt(
        password.encode("utf-8"), salt=salt.encode("utf-8"), n=16384, r=8, p=1, dklen=64
    )
    # print(password)
    # print(f"{hashed_password.hex()}.{salt}")
    return f"{hashed_password.hex()}.{salt}"
hashed_password = get_hashed_password(password)
print('the hashed password: ' + hashed_password)
