from graphql_jwt.utils import jwt_payload

def my_jwt_payload(user, context=None):
    payload = jwt_payload(user, context)

    # Adicione informações adicionais aqui
    payload['username'] = user.username
    payload['email'] = user.email
    # Adicione outros campos conforme necessário

    return payload