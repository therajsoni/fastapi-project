import jwt

from fastapi import Request, HTTPException

from app.core.config import SECRET_TOKEN, ALGORITHM


def create_token(payload):

    token = jwt.encode(
        payload,
        SECRET_TOKEN,
        algorithm=ALGORITHM
    )

    return token


def verify_token(token):

    return jwt.decode(
        token,
        SECRET_TOKEN,
        algorithms=[ALGORITHM]
    )


def bearer_token_verify(request: Request):

    authorization = request.headers.get("Authorization")

    if not authorization:
        raise HTTPException(
            status_code=401,
            detail="Authorization header required"
        )

    try:

        scheme, token = authorization.split(" ", 1)

        if scheme.lower() != "bearer":
            raise HTTPException(
                status_code=401,
                detail="Invalid authentication scheme"
            )

        return verify_token(token)

    except jwt.ExpiredSignatureError:

        raise HTTPException(
            status_code=401,
            detail="Token expired"
        )

    except jwt.InvalidTokenError:

        raise HTTPException(
            status_code=401,
            detail="Invalid token"
        )