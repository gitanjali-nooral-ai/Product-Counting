from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field

import yaml
from pathlib import Path

from config.settings import settings


router = APIRouter(
    prefix="/settings",
    tags=["Settings"]
)



class SettingsUpdate(BaseModel):

    camera_source: str | int | None = None

    confidence: float | None = Field(
        None,
        ge=0.1,
        le=1.0
    )

    image_size: int | None = Field(
        None,
        ge=160,
        le=1280
    )

    line_position: int | None = Field(
        None,
        ge=0
    )

    model_device: str | None = None



@router.get("/")
def get_settings():

    try:

        return {

            "camera":
                getattr(settings, "camera", {}),

            "model":
                getattr(settings, "model", {}),

            "counting":
                getattr(settings, "counting", {}),

            "storage":
                getattr(settings, "storage", {}),

            "database":
                getattr(settings, "database", {})

        }


    except Exception as e:

        raise HTTPException(

            status_code=500,

            detail=str(e)

        )





@router.put("/")
def update_settings(
    data: SettingsUpdate
):

    if not hasattr(settings, "config"):

        raise HTTPException(

            status_code=500,

            detail="Settings configuration object missing"

        )


    config = settings.config



    if data.camera_source is not None:

        config.setdefault(
            "camera",
            {}
        )

        config["camera"]["source"] = data.camera_source



    if data.confidence is not None:

        config.setdefault(
            "model",
            {}
        )

        config["model"]["confidence"] = data.confidence



    if data.image_size is not None:

        config.setdefault(
            "model",
            {}
        )

        config["model"]["image_size"] = data.image_size



    if data.model_device is not None:

        config.setdefault(
            "model",
            {}
        )

        config["model"]["device"] = data.model_device



    if data.line_position is not None:

        config.setdefault(
            "counting",
            {}
        )

        config["counting"]["line_position"] = data.line_position



    save_config(config)


    if hasattr(settings, "reload"):

        settings.reload()



    return {

        "message":
            "Settings updated successfully",

        "settings":
            config

    }





def save_config(config):


    config_file = (

        Path(__file__)
        .resolve()
        .parents[2]
        /
        "config"
        /
        "config.yaml"

    )


    if not config_file.exists():

        raise HTTPException(

            status_code=500,

            detail=f"Config file missing: {config_file}"

        )



    with open(
        config_file,
        "w"
    ) as file:

        yaml.safe_dump(

            config,

            file,

            sort_keys=False

        )