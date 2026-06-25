from fastapi import FastAPI

from api.routes import products
from api.routes import camera
from api.routes import reports



app = FastAPI(

    title="Customer Product Detection API",

    version="1.0"

)



app.include_router(

    products.router

)


app.include_router(

    camera.router

)


app.include_router(

    reports.router

)



@app.get("/")
def home():


    return {

        "application":

        "Customer Product Detection System",


        "status":

        "running"

    }