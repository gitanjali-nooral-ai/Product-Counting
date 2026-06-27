class ProductService:


    def __init__(self, database):

        self.database = database



    def register_product(
        self,
        name,
        image_path
    ):

        product_id = self.database.add_product(
            name,
            image_path
        )


        return {

            "id": product_id,

            "name": name,

            "image": image_path

        }