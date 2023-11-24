import graphene
from graphene_django import DjangoObjectType
from api.models import CustomUser
from api.types import UserType


class CreateUser(graphene.Mutation):
    class Arguments:
        email = graphene.String(required=True)
        password = graphene.String(required=True)

    # O tipo de retorno da mutação
    user = graphene.Field(UserType)  # UserType é um DjangoObjectType que você precisa definir para o modelo User

    @staticmethod
    def mutate(root, info, email, password):
        user = CustomUser.objects.create_user(email=email, password=password)
        return CreateUser(user=user)