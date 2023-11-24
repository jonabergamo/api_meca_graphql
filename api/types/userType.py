from api.models import CustomUser
from graphene_django import DjangoObjectType

class UserType(DjangoObjectType):
    class Meta:
        model = CustomUser
        fields = ('id', 'email', 'is_staff') # Inclua os campos que você deseja expor via GraphQL
