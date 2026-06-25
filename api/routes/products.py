from fastapi import APIRouter, UploadFile, File, Form

import os
import shutil



from src.database.sqlite_manager import Database

from services.product_service import ProductService



router = APIRouter(

    prefix="/products",

    tags=["Products"]

)



database = Database(

    "data/database/production.db"

)


service = ProductService(

    database

)



@router.post("/upload")
async def upload_product(

    name:str = Form(...),

    image:UploadFile = File(...)

):


    os.makedirs(

        "temp",

        exist_ok=True

    )


    file_path = (

        "temp/"

        +

        image.filename

    )



    with open(

        file_path,

        "wb"

    ) as buffer:


        shutil.copyfileobj(

            image.file,

            buffer

        )



    product_id = service.register_product(

        name,

        file_path

    )


    return {


        "message":

        "Product registered",


        "product_id":

        product_id

    }




@router.get("/")
def get_products():


    products = database.get_products()



    return {


        "products":

        products

    }