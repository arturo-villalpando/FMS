from app.models.Faq import Faq
from app.models.FaqCategory import FaqCategory
#
from app.graphql.faq.schema import FaqInput, FaqCategoryInput


class CreateMutation:

    def add_faq(self, data: FaqInput):
        faq = Faq()
        faq.faq = data.faq
        faq.save()

        return faq

    def add_faq_category(self, data: FaqCategoryInput):
        faq_category = FaqCategory()
        faq_category.category = data.category
        faq_category.save()

        return faq_category
