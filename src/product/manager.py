import os



class ProductManager:


    def __init__(self):

        os.makedirs(
            "data/products",
            exist_ok=True
        )



    def save(
        self,
        file
    ):


        path=f"data/products/{file.filename}"


        with open(path,"wb") as f:

            f.write(
                file.file.read()
            )


        return path
    