
from starlette.authentication import (
    AuthCredentials, AuthenticationBackend, AuthenticationError, SimpleUser
)
from app.logger import logger

#https://www.starlette.io/authentication/

class BasicAuth(AuthenticationBackend):
    async def authenticate(self, request):
        logger.info("Authenticating for request.path: " + request.url.path)
        if "Authorization" not in request.headers:
            return
        auth = request.headers["Authorization"]
        logger.info("Auth: " + auth)    
        if auth == "user:pass":
            return AuthCredentials(["authenticated"]), SimpleUser("user")
        else:
            raise AuthenticationError("Invalid basic auth credentials")
        
