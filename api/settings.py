from pydantic import BaseSettings


class APISettings(BaseSettings):
    HOST: str = '0.0.0.0'
    PORT: int = 8080
    DEBUG: bool = False
    RELOAD: bool = False


class PreProcessingSettings(BaseSettings):
    IMAGE_SHAPE = (45, 45, 1)
    IMAGE_SHAPE_WITHOUT_SHAPE = (45, 45)


class ModelSettings(BaseSettings):
    MODEL_WEIGHTS: str = '../notebooks/model.h5'


api = APISettings()
preprocessing = PreProcessingSettings()
model = ModelSettings()
