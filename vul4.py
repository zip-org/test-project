import jwt
from mysql.connector import connection

jwt.decode(token, options={"verify_signature": False})  # Noncompliant
jwt.decode(token, options={"verify_signature": False})  # Noncompliant
