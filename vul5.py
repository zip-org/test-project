import jwt

jwt.decode(token, options={"verify_signature":False}) # Noncompliant