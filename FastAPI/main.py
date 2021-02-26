import uvicorn
from fastapi import FastAPI

from starlette.requests import Request
from starlette.responses import Response

from core.db import SessionLocal
from routes import routes

app = FastAPI()

# middleware запускается на каждый запрос
@app.middleware("http")
async def db_session_middleware(request: Request, call_next):
    response = Response("Internal server error", status_code=500)
    try:
        request.state.db = SessionLocal()
        print('middleware sess open')
        response = await call_next(request)
    finally:
        print('middleware sess close')
        request.state.db.close()
    print('middleware ответ')
    return response


app.include_router(routes)

if __name__ == "__main__":
    uvicorn.run('main:app', host='0.0.0.0', port=8000, use_colors=True, reload=True)
