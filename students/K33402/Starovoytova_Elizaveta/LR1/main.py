from fastapi import FastAPI
import uvicorn
from database.conn import init_db
from endpoints.user import user_router


app = FastAPI()

app.include_router(user_router, prefix="/api", tags=["users"])


@app.on_event("startup")
def on_startup():
    init_db()


if __name__ == '__main__':
    uvicorn.run('main:app', host="localhost", port=8000, reload=True)
