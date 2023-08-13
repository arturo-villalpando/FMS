import strawberry
# List
from typing import List
from typing import Optional
# GraphQL
from .schema import FaqType
from .controller import Mutations, Queries


@strawberry.type
class Mutation:
    create_faq: FaqType = strawberry.mutation(resolver=Mutations.create_faq)
    update_faq: FaqType = strawberry.mutation(resolver=Mutations.update_faq)
    status_faq: FaqType = strawberry.mutation(resolver=Mutations.status_faq)


@strawberry.type
class Query:
    faqs: Optional[List[FaqType]] = strawberry.field(resolver=Queries.get_all_faqs)
    faq: Optional[FaqType] = strawberry.field(resolver=Queries.get_faq)
