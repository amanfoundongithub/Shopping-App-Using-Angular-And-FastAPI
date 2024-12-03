import bcrypt
import base64

def encrypt(password: str) -> str:
    hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    return base64.b64encode(hashed).decode('utf-8')

def verify(candidate: str, actual: str) -> bool:
    actual_bytes = base64.b64decode(actual.encode('utf-8'))
    return bcrypt.checkpw(candidate.encode(), actual_bytes)
