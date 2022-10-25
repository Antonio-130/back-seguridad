import bcrypt

def encrypt_password(password):
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt(13)).decode()

def compare_password(password, hashed):
    return bcrypt.checkpw(password.encode(), hashed.encode())