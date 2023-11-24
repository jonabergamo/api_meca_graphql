import graphene
from api.models import CustomUser
from api.types import UserType

class UserQuery(graphene.ObjectType):
    users = graphene.List(UserType)
    user = graphene.Field(UserType, id=graphene.Int())

    def resolve_all_users(self, info):
        user = info.context.user
        if not user.is_authenticated:
            raise Exception("Authentication credentials were not provided")
        return CustomUser.objects.all()


    def resolve_users(self, info):
        user = info.context.user
        if not user.is_authenticated:
            raise Exception("Authentication credentials were not provided")
        return CustomUser.objects.all()
    
    def resolve_user(self, info, id):
        user = info.context.user
        if not user.is_authenticated:
            raise Exception("Authentication credentials were not provided")
        try:
            return User.objects.get(pk=id)
        except CustomUser.DoesNotExist:
            return None
