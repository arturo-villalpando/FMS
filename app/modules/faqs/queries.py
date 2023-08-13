# Models
from models.Faq import Faq
# Builder
from masoniteorm.query import QueryBuilder
# Errors
from masoniteorm.exceptions import QueryException
from app.errors.custom import custom_graphql_error
from http import HTTPStatus


def get_all_faqs():
    faqs = Faq.with_({'category': lambda q: q.with_trashed()}).get()
    if not faqs or faqs is None:
        custom_graphql_error(
            message="Faqs not found",
            code="200",
            status=HTTPStatus.NOT_FOUND
        )
    return faqs


def get_all_active_faqs():
    builder = QueryBuilder(model=Faq)
    try:
        faqs = builder.statement(
            "SELECT * FROM faqs f \
                JOIN  faqs_categories fc ON fc.id = f.category_id \
                WHERE \
                f.deleted_at IS NULL AND fc.deleted_at IS NULL;"
        )
        if not faqs or faqs is None:
            custom_graphql_error(
                message="Faqs not found",
                code="200",
                status=HTTPStatus.NOT_FOUND
            )
        return faqs
    except QueryException as e:
        custom_graphql_error(
            message="Error trying to get faq",
            code=e.__cause__,
            status=HTTPStatus.BAD_REQUEST
        )


def get_faq_by_id(id: int):
    faq = Faq.with_({'category': lambda q: q.with_trashed()}).find(id)
    if not faq or faq is None:
        custom_graphql_error(
            message="Faq not found",
            code="",
            status=HTTPStatus.NOT_FOUND
        )

    return faq


def get_active_faq_by_id(id: int):
    builder = QueryBuilder(model=Faq)
    try:
        faq = builder.statement(
            "SELECT * FROM faqs f \
                JOIN  faqs_categories fc ON fc.id = f.category_id \
                WHERE \
                f.id = '?' AND f.deleted_at IS NULL AND fc.deleted_at IS NULL;"
        , [id])
        faq = Faq.find(id)
        if not faq or faq is None:
            custom_graphql_error(
                message="Faq not found",
                code="",
                status=HTTPStatus.NOT_FOUND
            )
        return faq
    except QueryException as e:
        custom_graphql_error(
            message="Error trying to get faq",
            code=e.__cause__,
            status=HTTPStatus.BAD_REQUEST
        )
