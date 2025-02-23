from fastapi import Depends, FastAPI, Request
from fastapi.responses import PlainTextResponse
from fastapi.security import APIKeyHeader
from app.todos import Priority, Todo, Todo_DB
from app.auth import BasicAuth
from app.logger import logger


#for http middleware
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.middleware.authentication import AuthenticationMiddleware

from app.middleware import log_middleware

from .routers import todo_routes 


"""
To run fast api woth uvicorn
fastapi dev main.py

To run gunicorn server with uvicorn workers
https://www.uvicorn.org/deployment/#gunicorn

gunicorn main:app --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000
"""

app = FastAPI()
logger.info("Starting FastAPI...")

# add middleware
app.add_middleware(BaseHTTPMiddleware,dispatch=log_middleware)

app.add_middleware(AuthenticationMiddleware, backend=BasicAuth())



# @app.middleware("http")
# async def add_process_time_header(request: Request, call_next):
#     log_dict = {
#         'url': request.url.path,
#         'method': request.method,
#     }
#     logger.info(log_dict)
#     response = await call_next(request)
#     return response



#Get the header form open ai docs

header_scheme = APIKeyHeader(name="Authorization")

app.include_router(todo_routes.router)


@app.get("/")
def root(request: Request, api_key: str = Depends(header_scheme)):
    if request.user.is_authenticated:
        return PlainTextResponse('Hello, ' + request.user.display_name)
    return PlainTextResponse('Hello, you')




