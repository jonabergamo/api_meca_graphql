import graphene
from graphene_django import DjangoObjectType
from django.contrib.auth.models import User
from api.types import UserType


class CreateUser(graphene.Mutation):
    class Arguments:
        username = graphene.String(required=True)
        email = graphene.String(required=True)
        password = graphene.String(required=True)

    # O tipo de retorno da mutação
    user = graphene.Field(UserType)  # UserType é um DjangoObjectType que você precisa definir para o modelo User

    @staticmethod
    def mutate(root, info, username, email, password):
        user = User.objects.create_user(username=username, email=email, password=password)
        return CreateUser(user=user)