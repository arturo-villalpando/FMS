from pydantic import BaseModel, Field


class BasicTranslate(BaseModel):
    lang: str = Field(min_length=2, max_length=2, default="es")
    name: str = Field(min_length=1)