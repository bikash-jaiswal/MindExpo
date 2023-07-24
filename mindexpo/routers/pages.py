from logging import Logger
from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import markdown
import frontmatter

router = APIRouter(
    prefix="/blogs",
    tags=["blog"],
    responses={404: {"description": "Not found"}},
)


templates = Jinja2Templates(directory="mindexpo/pages/templates")

@router.get("/", response_class=HTMLResponse)
async def root(request: Request):
    
    with open("mindexpo/pages/md_files/about_me.md", "r", encoding="utf-8") as input_file:
        metadata, content = frontmatter.parse(input_file.read())
    
    data = {
        "title": metadata['title'],
        "author": metadata['author'],
        "content": markdown.markdown(content)
    }
    return templates.TemplateResponse("about.html", {"request": request, "data": data})