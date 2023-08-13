import strawberry
# List
from typing import List
# GraphQL
from .schema import FaqCategoryType
from .controller import Mutations, Queries


@strawberry.type
class Mutation:
    create_faq_category: FaqCategoryType = strawberry.mutation(resolver=Mutations.create_faq_category)
    update_faq_category: FaqCategoryType = strawberry.mutation(resolver=Mutations.update_faq_category)
    status_faq_category: FaqCategoryType = strawberry.mutation(resolver=Mutations.status_faq_category)


@strawberry.type
class Query:
    faqs_categories: List[FaqCategoryType] = strawberry.field(resolver=Queries.get_all_faqs_categories)
    faq_category: FaqCategoryType = strawberry.field(resolver=Queries.get_faq_category)
