import json
# Models
from app.pydantic.faq_category import FaqCategoryModel
# Errors
from pydantic import ValidationError
from http import HTTPStatus
from app.errors.custom import custom_graphql_error
# [{"lang":"es","name":"Música"}]
# [{"lang":"es","name":"Música"},{"lang":"en","name":"Music"}]


def validate_faq_category(data: dict):
    try:
        FaqCategoryModel(
            category=json.loads(data.category)
        )
    except ValidationError as e:
        custom_graphql_error(
            message="Input should be a valid Faq Category",
            code=e.errors(),
            status=HTTPStatus.BAD_REQUEST
        )
