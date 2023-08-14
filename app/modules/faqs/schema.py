import strawberry

from typing import Optional
from datetime import datetime
from strawberry.scalars import JSON
# Relations
from app.modules.faqs_categories.schema import FaqCategoryType


@strawberry.type
class FaqType:
    id: int
    category: FaqCategoryType
    faq: JSON
    visits: int
    created_at: datetime
    updated_at: datetime
    deleted_at: Optional[datetime] = None


@strawberry.type
class FaqVisits:
    message: str = "Visits updated."


@strawberry.input
class FaqCreate:
    category_id: int
    faq: JSON


@strawberry.input
class FaqUpdate:
    id: int
    category_id: int
    faq: JSON
