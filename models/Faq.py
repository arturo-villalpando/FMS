""" Faq Model """
from masoniteorm.models import Model
from masoniteorm.scopes import SoftDeletesMixin
from masoniteorm.relationships import has_one

class Faq(Model, SoftDeletesMixin):
    """Faq Model"""
    __table__ = "faqs"

    __fillable__ = ["category_id","faq"]

    __casts__ = {"faq": "json"}

    __with__ = ['category']

    @has_one("id", "category_id")
    def category(self):
        from .FaqCategory import FaqCategory

        return FaqCategory
