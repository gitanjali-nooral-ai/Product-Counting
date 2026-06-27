import os
import shutil
import uuid

from config.settings import settings



class ProductService:


    def __init__(self, database):

        self.database = database



    def register_product(
        self,
        name,
        image_path
    ):


        product_folder = os.path.join(

            settings.storage["products"],

            name.replace(
                " ",
                "_"
            )

        )


        os.makedirs(

            product_folder,

            exist_ok=True

        )



        extension = os.path.splitext(
            image_path
        )[1].lower()



        filename = (

            str(uuid.uuid4())

            +

            extension

        )



        saved_image = os.path.join(

            product_folder,

            filename

        )



        shutil.copy(

            image_path,

            saved_image

        )



        product_id = self.database.add_product(

            name,

            saved_image

        )



        return {


            "id":

                product_id,


            "name":

                name,


            "image":

                saved_image

        }