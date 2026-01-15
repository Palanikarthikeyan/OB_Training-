from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/",response_class=HTMLResponse)
def f1():
    return "<h1><font color=green>Welcome to FastAPI</font></h1>"

@app.get("/mypage")
def f2():
    return HTMLResponse(content="<h2><font color=blue>Webpage resonse</font></h2>")

@app.get("/myview")
def f3():
    return HTMLResponse(
        content="<h2>Web page response</h2>",
        status_code=201,
        headers={"K1":"mywebpage"}
    )
