import torch
import clip

from PIL import Image
import numpy as np



class CLIPEncoder:


    def __init__(self):


        self.device="cpu"


        self.model,self.preprocess = clip.load(

            "ViT-B/32",

            device=self.device

        )



        self.model.eval()



    def encode_image(
        self,
        image_path
    ):


        image = Image.open(
            image_path
        ).convert(
            "RGB"
        )


        image=self.preprocess(
            image
        ).unsqueeze(0).to(
            self.device
        )


        with torch.no_grad():


            embedding=self.model.encode_image(

                image

            )


        embedding = embedding / embedding.norm(

            dim=-1,

            keepdim=True

        )


        return embedding.cpu().numpy()[0]



    def save_embedding(

        self,

        embedding,

        path

    ):


        np.save(

            path,

            embedding

        )



    def load_embedding(

        self,

        path

    ):


        return np.load(
            path
        )