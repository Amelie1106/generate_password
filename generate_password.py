import string
import secrets
import os
import hashlib
 
def generate_password(length=12):
    special_characters = '!"§$%&/()=?'
    alphabet = string.ascii_letters + string.digits + special_characters
    password = "".join(secrets.choice(alphabet) for i in range(length))
    return password
 
password = generate_password()
print('the password: ' + password)
 
def get_hashed_password(password):
    salt = os.urandom(8).hex()
    hashed_password = hashlib.scrypt(
        password.encode("utf-8"), salt=salt.encode("utf-8"), n=16384, r=8, p=1, dklen=64
    )
    return f"{hashed_password.hex()}.{salt}"
 
hashed_password = get_hashed_password(password)
print('the hashed password: ' + hashed_password)
