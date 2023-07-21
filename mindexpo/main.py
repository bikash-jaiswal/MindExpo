from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import markdown
from .routers import items, pages
from commonmark import commonmark
app = FastAPI()


app.include_router(pages.router)
app.include_router(items.router)



def marked_filter(text):
    return commonmark(text)

templates = Jinja2Templates(directory="mindexpo/pages/templates")
templates.env.filters['marked'] = marked_filter

@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    with open("mindexpo/pages/about_me.md", "r", encoding="utf-8") as input_file:
        text = input_file.read()
    html = markdown.markdown(text)

    data = {
        "title": "Somthing about me",
        "content": html
    }
    return templates.TemplateResponse("about.html", {"request": request, "data": data})
