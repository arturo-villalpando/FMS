from typing import List
import json
# Models
from models.Faq import Faq
# Schemas
from app.modules.faqs.schema import FaqType, FaqCreate, FaqUpdate, FaqVisits
# Queries
from .queries import get_all_faqs, get_all_active_faqs, \
    get_faq_by_id, get_active_faq_by_id, \
    get_faqs_by_categories, get_top_faqs, \
    update_stats
from app.modules.faqs_categories.queries import get_faq_category_by_id
# Helpers
from app.helpers.cleaner import json_cleaner_faqs
# Validations & Errors
from app.modules.faqs.validation import validate_faq
from app.errors.custom import custom_graphql_error
# Exceptions
from masoniteorm.exceptions import QueryException
from http import HTTPStatus


class Queries:
    # Multiple results
    def get_all_faqs(self, order:str='created_at', direction:str='desc') -> List[FaqType]:
        return get_all_faqs(order, direction)

    def get_all_faqs_by_category(self, category_id: int):
        return get_faqs_by_categories(category_id)

    def get_top_faqs(self):
        return get_top_faqs()

    # Single results
    def get_faq(self, id: int) -> FaqType:
        # Here we need to validate the use role, to check if has access to this endpoint (get_faq_category_by_id)...
        return get_active_faq_by_id(id)



class Mutations:
    def create_faq(self, data: FaqCreate) -> FaqType:
        # Validate model
        validate_faq(data)
        # Validate if the Faq Category exists
        faq_category = get_faq_category_by_id(data.category_id)
        # Clear JSON faq spaces with strip and convert to lowercase
        json_faq = json_cleaner_faqs(json.loads(data.faq))
        # Create the faq
        faq = Faq()
        faq.category_id = faq_category.id
        faq.faq = json.dumps(json_faq)
        try:
            faq.save()
        except QueryException as e:
            custom_graphql_error(
                message="Error trying to save faq",
                code=e.errors(),
                status=HTTPStatus.BAD_REQUEST
            )
        return faq

    def update_faq(self, data: FaqUpdate) -> FaqType:
        # Validate model
        validate_faq(data)
        # Validate if the Faq Category exists
        faq_category = get_faq_category_by_id(data.category_id)
        # Get the faq
        faq = get_faq_by_id(data.id)
        # Clear JSON faq spaces with strip and convert to lowercase
        json_faq = json_cleaner_faqs(json.loads(data.faq))
        # Update the faq
        faq.category_id = faq_category.id
        faq.faq = json.dumps(json_faq)
        # Save the changes
        try:
            faq.save()
        except Exception as e:
            custom_graphql_error(
                message="Error updating faq",
                code=e.errors(),
                status=HTTPStatus.BAD_REQUEST
            )
        return faq

    def status_faq(self, id: int) -> FaqType:
        # Get the faq
        faq = get_faq_by_id(id)
        try:
            if faq.deleted_at is None:
                faq.delete()
            else:
                faq.restore()
        except QueryException as e:
            custom_graphql_error(
                message="Failed to update faq status",
                code=e.__cause__,
                status=HTTPStatus.BAD_REQUEST
            )
        return faq

    def visits_faq(self, id: int) -> FaqVisits:
        update_stats(id)

        return FaqVisits