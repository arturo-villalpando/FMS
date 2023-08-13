import strawberry
# Faqs
from .faqs.core import Query as FaqQueries, Mutation as FaqMutations
# Faqs Categories
from .faqs_categories.core import Query as FaqCategoryQueries, Mutation as FaqCategoryMutations


@strawberry.type
class Query(
    FaqQueries,
    FaqCategoryQueries
):
    pass


@strawberry.type
class Mutation(
    FaqMutations,
    FaqCategoryMutations
):
    pass
