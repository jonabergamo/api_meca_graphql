import graphene
from graphene_django import DjangoObjectType
from api.models import IncubatorDevice, IncubatorSetting, CustomUser
from api.types import IncubatorDeviceType

class UpdateIncubatorDevice(graphene.Mutation):
    class Arguments:
        unique_id = graphene.String(required=True)
        user_id = graphene.Int()
        current_setting_id = graphene.Int()
        is_on = graphene.Boolean()
        humidity_sensor = graphene.String()
        temperature_sensor = graphene.String()

    # O tipo de retorno da mutação
    incubator_device = graphene.Field(IncubatorDeviceType)

    @staticmethod
    def mutate(root, info, unique_id, user_id=None, current_setting_id=None, is_on=None, humidity_sensor=None, temperature_sensor=None):
        user = info.context.user
        if not user.is_authenticated:
            raise Exception("Authentication credentials were not provided")
        try:
            device = IncubatorDevice.objects.get(unique_id=unique_id)
        except IncubatorDevice.DoesNotExist:
            return None

        if user_id is not None:
            device.user = CustomUser.objects.get(pk=user_id)
        if current_setting_id is not None:
            device.current_setting = IncubatorSetting.objects.get(pk=current_setting_id)
        if is_on is not None:
            device.is_on = is_on
        if humidity_sensor is not None:
            device.humidity_sensor = humidity_sensor
        if temperature_sensor is not None:
            device.temperature_sensor = temperature_sensor

        device.save()
        return UpdateIncubatorDevice(incubator_device=device)
