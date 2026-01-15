import uvicorn
import fastapi
app = fastapi.FastAPI()

@app.get("/")
async def f1():
    return {"Key1":"Welcome to FastAPI"}

if __name__ == '__main__':
    uvicorn.run("app6:app",reload=True)