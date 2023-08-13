from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime
# Models
from app.pydantic.faq_category import FaqCategoryModel
# Serializers
from app.pydantic.serializers.faq_tanslate import FaqTranslate


class FaqModel(BaseModel):
    category_id: int
    faq: List[FaqTranslate]


class UpdateFaqModel(BaseModel):
    category_id: Optional[int]
    faq: Optional[List[FaqTranslate]]
