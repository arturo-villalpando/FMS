import strawberry

from http import HTTPStatus
import json
# Errors and Builder
from graphql import GraphQLError
from masoniteorm.query import QueryBuilder
# Models
from app.models.Faq import Faq
from app.models.FaqCategory import FaqCategory
# Schemas
from app.graphql.faq.schema import FaqInput, FaqCategoryInput
# Validation
from pydantic import ValidationError
from app.graphql.faq.validation import FaqCategoryModel
# Helpers
from app.helpers.Cleaner import Cleaner


class CreateMutation:

    def add_faq(self, data: FaqInput):
        faq = Faq()
        faq.faq = data.faq
        faq.save()

        return faq


    def add_faq_category(self, data: FaqCategoryInput):
        # Validation
        try:
            FaqCategoryModel(
                category=json.loads(data.category)
            )
        except ValidationError:
             raise GraphQLError(
                 message="Input should be a valid list",
                 extensions={
                    "code": HTTPStatus.BAD_REQUEST
                }
             )
        # Clear JSON categories spaces with strip and convert category to lowercase
        cleaner = Cleaner
        category = cleaner.json_cleaner(json.loads(data.category))
        # Find if already exists a category
        builder = QueryBuilder(model=FaqCategory)
        for cat in category:
            faq_category = builder.statement(
                "SELECT id FROM faqs_categories WHERE category @> \'[{\"name\": \""+cat['name']+"\"}]\'"
            )
            if faq_category is not None:
                raise GraphQLError(
                    message="Category already exists!",
                    extensions={
                        "code": HTTPStatus.BAD_REQUEST
                    }
                )
        # If pass create json category
        faq_category = FaqCategory()
        faq_category.category = json.dumps(category)
        faq_category.save()

        return faq_category
