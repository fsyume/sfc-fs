from fastapi import APIRouter
from starlette.responses import RedirectResponse

router = APIRouter()


@router.get("/")
async def jump_blog():
    # 301 永久重定向
    return RedirectResponse("https://www.fsyume.com", status_code=301)


@router.get("/github")
async def jump_github():
    # 301 永久重定向
    return RedirectResponse("https://github.com/fsyume", status_code=301)


@router.get("/steam")
async def jump_steam():
    # 301 永久重定向
    return RedirectResponse("https://steamcommunity.com/profiles/76561198411546921", status_code=301)


@router.get("/bilibili")
async def jump_steam():
    # 301 永久重定向
    return RedirectResponse("https://space.bilibili.com/115505904", status_code=301)
