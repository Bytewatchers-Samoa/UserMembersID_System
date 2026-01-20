from datetime import datetime, timedelta
from jose import JWTError, jwt

SECRET_KEY = "placeholder_secret_key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60
