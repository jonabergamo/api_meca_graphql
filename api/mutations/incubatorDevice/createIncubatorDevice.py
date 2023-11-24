import graphene
from graphene_django import DjangoObjectType
from api.models import IncubatorDevice, CustomUser
from api.querys.incubatorDeviceQuery import IncubatorDeviceType
# Importe qualquer outro modelo necessário

class CreateIncubatorDevice(graphene.Mutation):
    class Arguments:
        # Defina aqui os argumentos necessários para criar um IncubatorDevice
        user_id = graphene.Int(required=True)
        humidity_sensor = graphene.String(required=True)
        temperature_sensor = graphene.String(required=True)

    # O tipo de retorno da mutação
    incubator_device = graphene.Field(IncubatorDeviceType)

    @staticmethod
    def mutate(root, info, user_id, humidity_sensor, temperature_sensor):
        user = CustomUser.objects.get(pk=user_id)
        user = info.context.user
        if not user.is_authenticated:
            raise Exception("Authentication credentials were not provided")
        incubator_device = IncubatorDevice(
            user=user,
            humidity_sensor=humidity_sensor,
            temperature_sensor=temperature_sensor
        )
    
        incubator_device.save()

        return CreateIncubatorDevice(incubator_device=incubator_device)
