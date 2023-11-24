import graphene
from api.models import IncubatorDevice
from api.types import IncubatorDeviceType


class IncubatorDeviceQuery(graphene.ObjectType):
    all_incubator_devices = graphene.List(IncubatorDeviceType)
    incubator_device = graphene.Field(IncubatorDeviceType, unique_id=graphene.String())

    def resolve_all_incubator_devices(self, info):
        # Retorna todos os dispositivos
        return IncubatorDevice.objects.all()

    def resolve_incubator_device(self, info, unique_id):
        # Retorna um dispositivo específico pelo seu unique_id
        try:
            return IncubatorDevice.objects.get(unique_id=unique_id)
        except IncubatorDevice.DoesNotExist:
            return None