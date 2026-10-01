import bcrypt

def hashPassword(password):
    hashed = bcrypt.hashpw(
        password.encode() , 
        bcrypt.gensalt(10)
    ).decode()
    return hashed

def verifyPassword(password , hashPassword):
    return bcrypt.verify(password , hashPassword)
    
          
