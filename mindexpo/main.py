from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import markdown
import uvicorn
from .routers import pages
import frontmatter

app = FastAPI()
app.mount("/static", StaticFiles(directory="mindexpo/static"), name="static")

app.include_router(pages.router)


templates = Jinja2Templates(directory="mindexpo/pages/templates")


# @app.get("/", response_class=HTMLResponse)
# async def root(request: Request):
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


def start():
    """Launched with `poetry run start` at root level"""
    uvicorn.run("mindexpo.main:app", reload=True, port=8001)
