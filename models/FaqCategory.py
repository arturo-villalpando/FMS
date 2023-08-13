""" faqs Model """
from masoniteorm.models import Model
from masoniteorm.scopes import SoftDeletesMixin


class FaqCategory(Model, SoftDeletesMixin):
    """Faqs Categories Model"""
    __table__ = "faqs_categories"

    __fillable__ = ["category"]

    __cast__ = {"category": "json"}
