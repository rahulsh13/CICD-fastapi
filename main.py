from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def get_homepage():
    return {'message': 'Home Page'}