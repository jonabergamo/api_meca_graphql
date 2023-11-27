from api.models import User
from graphene_django import DjangoObjectType

class UserType(DjangoObjectType):
    class Meta:
        model = User
        fields = ('id', 'email', 'is_staff','username','first_name','last_name' ) # Inclua os campos que você deseja expor via GraphQL
