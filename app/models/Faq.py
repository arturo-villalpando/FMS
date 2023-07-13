""" Faq Model """

from masoniteorm.models import Model


class Faq(Model):
    """Faq Model"""
    __table__ = "faqs"

    __guarded__ = ["id"]

    __dates__ = ["deleted_at"]

    __casts__ = {"faq": "json"}
