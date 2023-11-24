import graphene
from api.types import IncubatorSettingType
from api.models import IncubatorSetting

class IncubatorSettingQuery(graphene.ObjectType):
    all_incubator_settings = graphene.List(IncubatorSettingType)
    incubator_setting = graphene.Field(IncubatorSettingType, id=graphene.Int())

    def resolve_all_incubator_settings(self, info):
        # Retorna todas as configurações de incubadora
        return IncubatorSetting.objects.all()

    def resolve_incubator_setting(self, info, id):
        # Retorna uma configuração específica pelo seu ID
        try:
            return IncubatorSetting.objects.get(pk=id)
        except IncubatorSetting.DoesNotExist:
            return None
