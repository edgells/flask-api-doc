from fastapi import FastAPI, Query, Depends
from pydantic import BaseModel
from uvicorn import run


app = FastAPI()

class UserParams(BaseModel):
    username: str = Query(None, required=True,title="用户名称", alias="nickname")


@app.get("/")
def index(user: UserParams = Depends()):
    return {"data": "index"}


if __name__ == '__main__':
    run(app)