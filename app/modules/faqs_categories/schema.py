import strawberry

from typing import Optional
from datetime import datetime
from strawberry.scalars import JSON


@strawberry.type
class FaqCategoryType:
    id: int
    category: JSON
    created_at: datetime
    updated_at: datetime
    deleted_at: Optional[datetime] = None


@strawberry.input
class FaqCategoryCreate:
    category: JSON


@strawberry.input
class FaqCategoryUpdate:
    id: int
    category: JSON
