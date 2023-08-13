# Models
from models.FaqCategory import FaqCategory
# Builder
from masoniteorm.query import QueryBuilder
# Errors
from app.errors.custom import custom_graphql_error
from http import HTTPStatus


def get_all_faq_categories():
    return FaqCategory.with_trashed().all()


def get_all_active_faq_categories():
    return FaqCategory.all()


def get_faq_category_by_id(id: int):
    faq_category = FaqCategory.with_trashed().find(id)
    if not faq_category:
        custom_graphql_error(
            message="Faq category not found",
            code="",
            status=HTTPStatus.NOT_FOUND
        )
    return faq_category


def get_active_faq_category_by_id(id: int):
    faq_category = FaqCategory.find(id)
    if not faq_category:
        custom_graphql_error(
            message="Faq category not found",
            code="",
            status=HTTPStatus.NOT_FOUND
        )

    return faq_category


def exists_faq_category_by_name(category: dict):
    builder = QueryBuilder(model=FaqCategory)
    for cat in category:
        faq_category = builder.statement(
            "SELECT id FROM faqs_categories WHERE category @> \'[{\"name\": \"" + cat['name'] + "\"}]\'"
        )
        if faq_category is not None:
            custom_graphql_error(
                message="Faq category '" + cat['name'] + "' already exists",
                code="",
                status=HTTPStatus.FOUND
            )
    return True


def exists_faq_category_by_name_id(id: int, category: dict):
    builder = QueryBuilder(model=FaqCategory)
    for cat in category:
        search_faq_category = builder.statement(
            "SELECT id FROM faqs_categories WHERE category @> \'[{\"name\": \"" + cat[
                'name'] + "\"}]\' AND id != '?'", [id]
        )
        if search_faq_category is not None:
            custom_graphql_error(
                message="Faq category '" + cat['name'] + "' already exists",
                code="",
                status=HTTPStatus.FOUND
            )
    return True
