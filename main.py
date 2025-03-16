from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def get_homepage():
    return {'message': 'Home Page'}

@app.get('/about')
def get_aboutpage():
    return {'message': 'About page'}