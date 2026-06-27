from pathlib import Path
import yaml


class Settings:


    def __init__(self):

        file=Path(__file__).parent/"config.yaml"

        with open(file) as f:

            self.data=yaml.safe_load(f)



    @property
    def camera(self):

        return self.data["camera"]



    @property
    def model(self):

        return self.data["model"]



    @property
    def database(self):

        return self.data["database"]



settings=Settings()