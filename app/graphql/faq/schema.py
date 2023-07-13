import strawberry
# Import optional and List
from typing import List, Optional
# Import types
from datetime import datetime
from strawberry.scalars import JSON


#
# Faq
#
@strawberry.type
class FaqType:
    id: int
    faq: JSON
    deleted_at: Optional[datetime]


@strawberry.input
class FaqInput:
    faq: Optional[JSON]
    deleted_at: Optional[datetime]


#
# Faq Category
#
@strawberry.type
class FaqCategoryType:
    id: int
    category: JSON
    deleted_at: Optional[datetime]


@strawberry.input
class FaqCategoryInput:
    category: Optional[JSON]
    deleted_at: Optional[datetime]
