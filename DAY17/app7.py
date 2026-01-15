from fastapi import FastAPI

app = FastAPI()

@app.get("/mypage")
async def f1(n:str,c:int):
    name = n
    code = c
    return {"name": name,"code": code}

