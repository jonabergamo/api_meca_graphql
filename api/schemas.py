import graphene
from api.querys import UserQuery, IncubatorDeviceQuery, IncubatorSettingQuery
from api.mutations import CreateIncubatorDevice, CreateUser, CreateIncubatorSetting, UpdateIncubatorSetting, UpdateIncubatorDevice, DeleteIncubatorSetting, DeleteUser, UpdateUser


class Query(UserQuery,IncubatorSettingQuery, IncubatorDeviceQuery, graphene.ObjectType ):
    pass

class Mutation(graphene.ObjectType):
    create_incubator_device = CreateIncubatorDevice.Field()
    update_incubator_device = UpdateIncubatorDevice.Field()

    create_user = CreateUser.Field()
    delete_user = DeleteUser.Field()
    update_user = UpdateUser.Field()
    
    create_incubator_setting = CreateIncubatorSetting.Field()
    update_incubator_setting = UpdateIncubatorSetting.Field()
    delete_incubator_setting = DeleteIncubatorSetting.Field()
    
    

schema = graphene.Schema(query=Query, mutation=Mutation)
