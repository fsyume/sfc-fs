from fastapi import APIRouter

router = APIRouter()


@router.get("/images/test")
async def images_test():
    # 301 永久重定向
    return {"msg": "hello this is imagesAPI"}
