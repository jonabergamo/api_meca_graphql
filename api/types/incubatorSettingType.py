import graphene
from graphene_django import DjangoObjectType
from api.models import IncubatorSetting, User


class IncubatorSettingType(DjangoObjectType):
    class Meta:
        model = IncubatorSetting
        fields = '__all__'