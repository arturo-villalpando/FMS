# Models
from models.Faq import Faq
# Errors
from app.errors.custom import custom_graphql_error
from http import HTTPStatus
# Exceptions
from masoniteorm.exceptions import QueryException


# Multiple Results
def get_all_faqs(order: str, direction: str):
    faqs = Faq.with_trashed().with_({'category': lambda q: q.with_trashed()}).order_by(order, direction).get()
    if not faqs or faqs is None:
        custom_graphql_error(
            message="Faqs not found",
            code="Not Found!",
            status=HTTPStatus.NOT_FOUND
        )
    return faqs


def get_all_active_faqs(order: str, direction: str):
    faqs = Faq.join_on('category', lambda q: q.where_null('deleted_at')).order_by(order, direction).get()
    if not faqs or faqs is None:
        custom_graphql_error(
            message="Faqs not found",
            code="Not Found!",
            status=HTTPStatus.NOT_FOUND
        )
    return faqs


# These queries are just for "active" records
def get_faqs_by_categories(category_id: int):
    faqs = Faq.join_on('category', lambda q: q.where('id', category_id).where_null('deleted_at')).order_by("visits", "desc").get()
    if not faqs or faqs is None:
        custom_graphql_error(
            message="Faqs not found",
            code="Not Found!",
            status=HTTPStatus.NOT_FOUND
        )
    return faqs


def get_top_faqs():
    faqs = Faq.join_on('category', lambda q: q.where_null('deleted_at')).order_by('visits', 'desc').first(5).get()
    if not faqs or faqs is None:
        custom_graphql_error(
            message="Faqs not found",
            code="Not Found!",
            status=HTTPStatus.NOT_FOUND
        )
    return faqs


# Single Results
def get_faq_by_id(id: int):
    faq = Faq.with_trashed().with_({'category': lambda q: q.with_trashed()}).find(id)
    if not faq or faq is None:
        custom_graphql_error(
            message="Faq not found",
            code="Not Found!",
            status=HTTPStatus.NOT_FOUND
        )
    return faq


def get_active_faq_by_id(id: int):
    faq = Faq.join_on('category', lambda q: q.where_null('deleted_at')).find(id)
    if not faq or faq is None:
        custom_graphql_error(
            message="Faq not found",
            code="Not Found!",
            status=HTTPStatus.NOT_FOUND
        )
    return faq


# Update Stats
def update_stats(id: int):
    faq = Faq.find(id)
    if not faq or faq is None:
        custom_graphql_error(
            message="Faq not found",
            code="Not Found!",
            status=HTTPStatus.NOT_FOUND
        )
    # Increment and save the changes
    try:
        faq.visits = faq.visits + 1
        faq.save()
    except QueryException as e:
        custom_graphql_error(
            message="Failed to update faq status",
            code=e.__cause__,
            status=HTTPStatus.BAD_REQUEST
        )
    return True

