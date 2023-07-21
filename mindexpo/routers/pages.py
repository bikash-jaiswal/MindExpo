from fastapi import APIRouter

router = APIRouter(
    prefix="/blogs",
    tags=["blog"],
    responses={404: {"description": "Not found"}},
)

@router.get("/")
async def pages():
    return {"Hello World"}
