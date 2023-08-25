from logging import Logger
from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException, Request

# from fastapi.responses import HTMLResponse
# from fastapi.templating import Jinja2Templates
import markdown
import frontmatter
from mindexpo.db.database import BlogPost as blog_db, SessionLocal, add_blog
from mindexpo.db import schemas
from sqlalchemy.orm import Session
router = APIRouter(
    prefix="/blogs",
    tags=["blog"],
    responses={404: {"description": "Not found"}},
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated(Session, Depends(get_db))

@router.get('/')
async def read_all(db: db_dependency):
    return db.query(schemas.BlogPost).all

@router.get("/{title}", response_model=schemas.BlogPost)
def read_blogpost(title: str):
    db = SessionLocal()
    blogpost = db.query(blog_db).filter(blog_db.title == title).first()
    db.close()
    if blogpost is None:
        raise HTTPException(status_code=404, detail="Blog post not found")
    return blogpost


@router.post("/")
def add_blogpost(request: schemas.BlogPost):
    add_blog(request.BlogPost)
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
