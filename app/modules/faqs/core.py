import strawberry
# List
from typing import List
# GraphQL
from .schema import FaqType, FaqVisits
from .controller import Mutations, Queries


@strawberry.type
class Mutation:
    create_faq: FaqType = strawberry.mutation(resolver=Mutations.create_faq)
    update_faq: FaqType = strawberry.mutation(resolver=Mutations.update_faq)
    status_faq: FaqType = strawberry.mutation(resolver=Mutations.status_faq)

    visits_faq: FaqVisits = strawberry.mutation(resolver=Mutations.visits_faq)


@strawberry.type
class Query:
    faq: FaqType = strawberry.field(resolver=Queries.get_faq)
    faqs: List[FaqType] = strawberry.field(resolver=Queries.get_all_faqs)

    faqs_by_category: List[FaqType] = strawberry.field(resolver=Queries.get_all_faqs_by_category)
    faqs_top:  List[FaqType] = strawberry.field(resolver=Queries.get_top_faqs)
