import uvicorn
from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder

from starlette.requests import Request
from starlette.responses import Response, JSONResponse

from core.db import SessionLocal
from routes import routes

# CORS
from fastapi.middleware.cors import CORSMiddleware


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

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get('/home', status_code=200)
def ret():
    content = {"message": "Hello World"}
    headers = {"X-Cat-Dog": "alone in the world", "Content-Language": "en-US"}
    return JSONResponse(content=content, headers=headers)


if __name__ == "__main__":
    uvicorn.run('main:app', host='0.0.0.0', port=8000, use_colors=True, reload=True)
