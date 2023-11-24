import graphene
from api.models import User
from api.types import UserType

class UserQuery(graphene.ObjectType):
    users = graphene.List(UserType)
    user = graphene.Field(UserType, id=graphene.Int())

    
    def resolve_all_users(self, info):
        # Retorna todos os users
        return User.objects.all()


    def resolve_users(self, info):
        # Aqui, você pode adicionar qualquer lógica de filtragem que desejar
        return User.objects.all()
    
    def resolve_user(self, info, id):
        # Retorna uma configuração específica pelo seu ID
        try:
            return User.objects.get(pk=id)
        except User.DoesNotExist:
            return None
