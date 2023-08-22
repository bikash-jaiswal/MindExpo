from logging import Logger
from fastapi import APIRouter, HTTPException, Request

# from fastapi.responses import HTMLResponse
# from fastapi.templating import Jinja2Templates
import markdown
import frontmatter
from mindexpo.db.database import BlogPost, SessionLocal
from mindexpo.db import schemas

router = APIRouter(
    prefix="/blogs",
    tags=["blog"],
    responses={404: {"description": "Not found"}},
)


@router.get("/{blogpost_id}", response_model=schemas.BlogPost)
def read_blogpost(blogpost_id: int):
    db = SessionLocal()
    blogpost = db.query(BlogPost).filter(BlogPost.id == blogpost_id).first()
    db.close()
    if blogpost is None:
        raise HTTPException(status_code=404, detail="Blog post not found")
    return blogpost


@router.post("/")
def add_blogpost(request: schemas.BlogPost):
    return f"New Post added: {request.id}, {request.title}, {request.content}, {request.created_at}"


# templates = Jinja2Templates(directory="mindexpo/pages/templates")


# @router.get("/", response_class=HTMLResponse)
# async def root(request: Request):
#     # run_db()
#     with open(
#         "mindexpo/pages/md_files/about_me.md", "r", encoding="utf-8"
#     ) as input_file:
#         metadata, content = frontmatter.parse(input_file.read())

#     data = {
#         "title": metadata["title"],
#         "author": metadata["author"],
#         "content": markdown.markdown(content),
#     }
#     return templates.TemplateResponse("about.html", {"request": request, "data": data})
