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


UPLOAD_FOLDER = "uploads/products"


os.makedirs(
    UPLOAD_FOLDER,
    exist_ok=True
)




# -----------------------------------
# Upload Product
# -----------------------------------

@router.post("/upload")
async def upload_product(

    name: str = Form(...),

    image: UploadFile = File(...)

):


    extension = os.path.splitext(
        image.filename
    )[1].lower()



    if extension not in ALLOWED_EXTENSIONS:

        raise HTTPException(

            status_code=400,

            detail="Only jpg, jpeg, png images allowed"

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

        "message":
            "Product registered successfully",

        "product":
            product

    }





# -----------------------------------
# Get Products
# -----------------------------------

@router.get("/")
def get_products():


    cursor = database.conn.cursor()



    rows = cursor.execute(

        """

        SELECT

            id,

            name,

            image,

            created


        FROM products


        ORDER BY id DESC

        """

    ).fetchall()



    products = []



    for row in rows:

        products.append({

            "id": row[0],

            "name": row[1],

            "image": row[2],

            "created": row[3]

        })



    return {

        "total": len(products),

        "products": products

    }