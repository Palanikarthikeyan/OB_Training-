from fastapi import FastAPI,Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory="templates")

@app.get("/",response_class=HTMLResponse)
def f1(request: Request):
    return templates.TemplateResponse(
        "mypage.html",
        {"request":request,"title_var":"FastAPI Page","course":"FullStackWebApp"}
    )
    
    
# Run as: python -m uvicorn app10:app --reload