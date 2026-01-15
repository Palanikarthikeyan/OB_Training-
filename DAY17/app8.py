from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()
'''
@app.get("/")
def f1():
    return "<h1>Hello FastAPI</h1>"
'''
@app.get("/",response_class = HTMLResponse)
def f1():
    return "<h1>Hello FastAPI</h1>"
