from pydantic import BaseModel, Field


class FaqTranslate(BaseModel):
    lang: str = Field(min_length=2, max_length=2, default="es")
    question: str = Field(min_length=2, max_length=64)
    answer: str = Field(min_length=2)
