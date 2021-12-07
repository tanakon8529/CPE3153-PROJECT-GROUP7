from libs.mysqldb import search_database, str_on_page
from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import uvicorn


app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templeates/")


@app.get("/")
async def index(request: Request):
    return dict(hello="CPE3153 - Hello world")


@app.get("/search", response_class=HTMLResponse)
async def search_form(request: Request):
    result = ""
    return templates.TemplateResponse("search.html", context={'request': request, 'result' : result})


@app.post("/search")
async def search_fill(request: Request, str_fill: str = Form(...)):
    query = search_database(str_fill)
    result = str_on_page(query)
    return templates.TemplateResponse("search.html", context={'request': request,'result' : result})


if __name__ == '__main__':
    uvicorn.run(app)

