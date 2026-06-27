from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager

from api.routes import products
from api.routes import camera
from api.routes import reports
from api.routes import settings
from api.routes import statistics
from api.routes import dashboard
from api.routes import health
from api.routes import stream
from api.routes import snapshot
from api.routes import events


@asynccontextmanager
async def lifespan(app: FastAPI):

    print("================================")
    print( "Customer Product Detection API")
    print( "YOLO11n Pipeline Starting")
    print("================================")

    yield
    
    print("API shutting down")





app = FastAPI(

    title="Customer Product Detection API",

    version="2.0.0",

    description="YOLO11n based customer product counting system",

    lifespan=lifespan

)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


app.include_router(products.router)
app.include_router(camera.router)
app.include_router(stream.router)
app.include_router(snapshot.router)
app.include_router(reports.router)
app.include_router(statistics.router)
app.include_router(dashboard.router)
app.include_router(health.router)
app.include_router(events.router)
app.include_router(settings.router)



@app.get("/")
def home():

    return {
        "application":"Customer Product Detection System",

        "engine": "YOLO11n + ByteTrack",

        "status": "running",

        "version":"2.0.0"
    }