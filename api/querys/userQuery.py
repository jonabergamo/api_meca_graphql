import graphene
from api.models import User
from api.types import UserType

class UserQuery(graphene.ObjectType):
    users = graphene.List(UserType)

    def resolve_users(self, info):
        # Aqui, você pode adicionar qualquer lógica de filtragem que desejar
        return User.objects.all()
