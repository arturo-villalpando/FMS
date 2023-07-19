from pydantic import BaseModel, ValidationError, field_validator
from typing import List
# Serializers
from app.validations.basic_translate import BasicTranslate


class FaqCategoryModel(BaseModel):
    category: List[BasicTranslate]

