from api.models import User
from graphene_django import DjangoObjectType

class UserType(DjangoObjectType):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'is_staff') # Inclua os campos que você deseja expor via GraphQL
