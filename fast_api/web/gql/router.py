import strawberry
from strawberry.fastapi import GraphQLRouter

from fast_api.web.gql import dummy, echo, rabbit, redis
from fast_api.web.gql.context import get_context


@strawberry.type
class Query(  # noqa: WPS215
    echo.Query,
    dummy.Query,
    redis.Query,
):
    """Main query."""


@strawberry.type
class Mutation(  # noqa: WPS215
    echo.Mutation,
    dummy.Mutation,
    redis.Mutation,
    rabbit.Mutation,
):
    """Main mutation."""


schema = strawberry.Schema(
    Query,
    Mutation,
)

gql_router = GraphQLRouter(
    schema,
    graphiql=True,
    context_getter=get_context,
)
