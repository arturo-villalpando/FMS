import strawberry

from app.graphql.faq.schema import FaqType, FaqCategoryType
from app.graphql.faq.controller import CreateMutation


@strawberry.type
class Mutation:
    add_faq: FaqType = strawberry.mutation(resolver=CreateMutation.add_faq)
    add_faq_category: FaqCategoryType = strawberry.mutation(resolver=CreateMutation.add_faq_category)
