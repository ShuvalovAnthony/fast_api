"""Redis API."""
from fast_api.web.gql.redis.mutation import Mutation
from fast_api.web.gql.redis.query import Query

__all__ = ["Query", "Mutation"]
