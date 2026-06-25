import os
import shutil


from src.embedding.clip_encoder import CLIPEncoder



class ProductService:


    def __init__(

        self,

        database

    ):


        self.database = database

        self.encoder = CLIPEncoder()



    def register_product(

        self,

        name,

        image_path

    ):


        # Create folders

        os.makedirs(

            "data/products/images",

            exist_ok=True

        )


        os.makedirs(

            "data/products/embeddings",

            exist_ok=True

        )



        # Copy image

        filename=os.path.basename(

            image_path

        )


        saved_image=os.path.join(

            "data/products/images",

            filename

        )


        shutil.copy(

            image_path,

            saved_image

        )



        # Generate embedding


        embedding=self.encoder.encode_image(

            saved_image

        )



        embedding_path=os.path.join(

            "data/products/embeddings",

            filename+".npy"

        )



        self.encoder.save_embedding(

            embedding,

            embedding_path

        )



        # Store database record


        product_id=self.database.add_product(

            name,

            saved_image,

            embedding_path

        )



        return product_id