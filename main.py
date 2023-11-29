import uvicorn
from fastapi import FastAPI

from routers import jump301, images

app = FastAPI()

# 路由引入
app.include_router(jump301.router)
app.include_router(images.router)


@app.get("/test")
async def test():
    return {"msg": "HELLO!!!"}


if __name__ == '__main__':
    uvicorn.run('main:app', host='0.0.0.0', port=9000)
