from fastapi import APIRouter, UploadFile, File, Form, HTTPException
import os
import shutil
import uuid

from src.database.database import Database
from config.settings import settings
from services.product_service import ProductService


router = APIRouter(
    prefix="/products",
    tags=["Products"]
)


database = Database(
    settings.database["path"]
)

service = ProductService(
    database
)


ALLOWED_EXTENSIONS = [
    ".jpg",
    ".jpeg",
    ".png"
]


UPLOAD_FOLDER = "data/products"


os.makedirs(
    UPLOAD_FOLDER,
    exist_ok=True
)



@router.post("/upload")
async def upload_product(
    name: str = Form(...),
    image: UploadFile = File(...)
):

    if not name.strip():
        raise HTTPException(
            status_code=400,
            detail="Product name required"
        )


    extension = os.path.splitext(
        image.filename
    )[1].lower()


    if extension not in ALLOWED_EXTENSIONS:

        raise HTTPException(
            status_code=400,
            detail="Only jpg, jpeg and png images allowed"
        )


    filename = (
        str(uuid.uuid4())
        +
        extension
    )


    file_path = os.path.join(
        UPLOAD_FOLDER,
        filename
    )


    try:

        with open(
            file_path,
            "wb"
        ) as buffer:

            shutil.copyfileobj(
                image.file,
                buffer
            )


        product = service.register_product(
            name,
            file_path
        )


        return {

            "message": "Product registered successfully",

            "product": product

        }


    except Exception as error:

        if os.path.exists(file_path):
            os.remove(file_path)

        raise HTTPException(
            status_code=500,
            detail=str(error)
        )




@router.get("/")
def get_products():

    products = database.get_products()


    return {

        "total": len(products),

        "products": products

    }