# coding: utf-8
from haystack import indexes

from pet import models


class MemberIndex(indexes.SearchIndex, indexes.Indexable):
    """
    Quantity fields: 21 fields
    """

    text = indexes.CharField(document=True, use_template=True)

    pet_id = indexes.CharField(null=True)

    name = indexes.CharField(model_attr="name", null=True)
    race = indexes.CharField(model_attr="race", null=True)
    age = indexes.CharField(model_attr="age", null=True)
    weight = indexes.CharField(model_attr="age", null=True)

    category = indexes.CharField(model_attr="category", null=True)

    city = indexes.CharField(model_attr="city", null=True)

    adopt_email = indexes.CharField(null=True)
    adopt_name = indexes.CharField(null=True)

    def get_model(self):
        return models.Pet

    def prepare_adopt_email(self, obj):
        return obj.creator.email

    def prepare_adopt_name(self, obj):
        return obj.creator.name

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.all()
