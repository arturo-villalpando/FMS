from pydantic import BaseModel
from typing import List
# Serializers
from .serializers.basic_translate import BasicTranslate


class FaqCategoryModel(BaseModel):
    category: List[BasicTranslate]
