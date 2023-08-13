import json
# Models
from app.pydantic.faq import FaqModel
# Errors
from pydantic import ValidationError
from http import HTTPStatus
from app.errors.custom import custom_graphql_error
# [{"lang":"es","question":"¿Hola?", "answer": "Hola mundo!"}]
# [{"lang":"es","question":"¿Hola?", "answer": "Hola mundo!"},{"lang":"en","question":"Hi?", "answer": "Hello World!"}]

def validate_faq(data: dict):
    try:
        FaqModel(
            category_id=data.category_id,
            faq=json.loads(data.faq)
        )
    except ValidationError as e:
        custom_graphql_error(
            message="Input should be a valid Faq",
            code=e.errors(),
            status=HTTPStatus.BAD_REQUEST
        )
