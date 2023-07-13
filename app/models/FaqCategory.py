""" FaqCategory Model """

import json

from masoniteorm.models import Model
from masoniteorm.relationships import has_many


class FaqCategory(Model):
    """FaqCategory Model"""
    __table__ = "faqs_categories"

    __guarded__ = ["id"]

    __dates__ = ["deleted_at"]

    __cast__ = {"category": "json"}

    @has_many("id", "category_id")
    def posts(self):
        from .Faq import Faq
