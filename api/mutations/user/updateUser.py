import graphene
from django.contrib.auth.models import User
from api.types import UserType

class UpdateUser(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        username = graphene.String()
        email = graphene.String()
        password = graphene.String()

    # O tipo de retorno da mutação
    user = graphene.Field(UserType)

    @staticmethod
    def mutate(root, info, id, username=None, email=None, password=None):
        try:
            user = User.objects.get(pk=id)

            if username is not None:
                user.username = username
            if email is not None:
                user.email = email
            if password is not None:
                user.set_password(password)

            user.save()
            return UpdateUser(user=user)

        except User.DoesNotExist:
            return None