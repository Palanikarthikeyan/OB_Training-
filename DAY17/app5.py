import uvicorn
import fastapi
app = fastapi.FastAPI()
'''
@app.get("/")
async def f1():
    return "<h1> Welcome to FastAPI</h1>"

if __name__ == '__main__':
    uvicorn.run("main:app",host="127.0.0.1", port= 8000,reload=True)
'''
@app.get("/")
def fx():
    return "Hello"

# Run this: python -m uvicorn app5:app --reload
