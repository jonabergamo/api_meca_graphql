import graphene
from api.models import IncubatorDevice

class DeleteIncubatorDevice(graphene.Mutation):
    class Arguments:
        unique_id = graphene.String(required=True)

    # O tipo de retorno da mutação
    success = graphene.Boolean()

    @staticmethod
    def mutate(root, info, unique_id):
        try:
            device = IncubatorDevice.objects.get(unique_id=unique_id)
            device.delete()
            return DeleteIncubatorDevice(success=True)
        except IncubatorDevice.DoesNotExist:
            # Retorna False se o dispositivo não for encontrado
            return DeleteIncubatorDevice(success=False)
