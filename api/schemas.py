import graphene
from api.querys import UserQuery, IncubatorDeviceQuery, IncubatorSettingQuery
from api.mutations import CreateIncubatorDevice, CreateUser, CreateIncubatorSetting, UpdateIncubatorSetting, UpdateIncubatorDevice


class Query(UserQuery,IncubatorSettingQuery, IncubatorDeviceQuery, graphene.ObjectType ):
    pass

class Mutation(graphene.ObjectType):
    create_incubator_device = CreateIncubatorDevice.Field()
    create_user = CreateUser.Field()
    create_incubator_setting = CreateIncubatorSetting.Field()
    update_incubator_setting = UpdateIncubatorSetting.Field()
    update_incubator_device = UpdateIncubatorDevice.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)