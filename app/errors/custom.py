from graphql import GraphQLError


def custom_graphql_error(message: str, code: str, status: str):
    raise GraphQLError(
        message=message,
        extensions={
            "code": code,
            "http": {
                "status": status
            }
        }
    )
