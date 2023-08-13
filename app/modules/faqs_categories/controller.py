from typing import List
import json
# Models
from models.FaqCategory import FaqCategory
# Schemas
from app.modules.faqs_categories.schema import FaqCategoryType, FaqCategoryCreate, FaqCategoryUpdate
# Queries
from .queries import get_all_active_faq_categories, \
    get_faq_category_by_id, get_active_faq_category_by_id, \
    exists_faq_category_by_name, exists_faq_category_by_name_id
# Helpers
from app.helpers.cleaner import json_cleaner_category
# Validations & Errors
from app.modules.faqs_categories.validation import validate_faq_category
from app.errors.custom import custom_graphql_error
# Exceptions
from masoniteorm.exceptions import QueryException
from http import HTTPStatus


class Queries:
    def get_all_faqs_categories(self) -> List[FaqCategoryType]:
        # Here we need validate the user role to call all active or all (get_all_faq_categories)...
        return get_all_active_faq_categories()

    def get_faq_category(self, id: int) -> FaqCategoryType:
        # Here we need to validate the use role, to check if has access to this endpoint (get_faq_category_by_id)...
        return get_active_faq_category_by_id(id)


class Mutations:
    def create_faq_category(self, data: FaqCategoryCreate) -> FaqCategoryType:
        # Validate model
        validate_faq_category(data)
        # Clear JSON categories spaces with strip and convert to lowercase
        category = json_cleaner_category(json.loads(data.category))
        # Find if already exists the category
        exists_faq_category_by_name(category)
        # Create the faq category
        faq_category = FaqCategory()
        faq_category.category = json.dumps(category)
        try:
            faq_category.save()
        except QueryException as e:
            custom_graphql_error(
                message="Error trying to save faq category",
                code=e.errors(),
                status=HTTPStatus.BAD_REQUEST
            )
        return faq_category

    def update_faq_category(self, data: FaqCategoryUpdate) -> FaqCategoryType:
        # Validate model
        validate_faq_category(data)
        # Get faq category
        faq_category = get_faq_category_by_id(data.id)
        # Clear JSON categories spaces with strip and convert to lowercase
        category = json_cleaner_category(json.loads(data.category))
        # Find if already exists the category
        exists_faq_category_by_name_id(data.id, category)
        # Update the faq category
        faq_category.category = json.dumps(category)
        # Save the changes
        try:
            faq_category.save()
        except Exception as e:
            custom_graphql_error(
                message="Error updating faq category",
                code=e.errors(),
                status=HTTPStatus.BAD_REQUEST
            )
        return faq_category

    def status_faq_category(self, id: int) -> FaqCategoryType:
        # Get the faq category
        faq_category = get_faq_category_by_id(id)
        try:
            if faq_category.deleted_at is None:
                faq_category.delete()
            else:
                faq_category.restore()
        except QueryException as e:
            custom_graphql_error(
                message="Failed to update faq category status",
                code=e.__cause__,
                status=HTTPStatus.BAD_REQUEST
            )
        return faq_category
