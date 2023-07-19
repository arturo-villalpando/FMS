import strawberry

from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter
#from strawberry.schema.base import BaseSchema
from app.base_schema import BaseSchema

from app.graphql.core import Mutation

# new
@strawberry.type
class Query:
  @strawberry.field
  def hello(self) -> str:
    return "Hello World"


# schema = strawberry.Schema(Query)  # new
#schema = strawberry.Schema(query=Query, mutation=Mutation)
# Production
schema = BaseSchema(query=Query, mutation=Mutation)

graphql_app = GraphQLRouter(schema)

# Start fastapi and include graphql to the router
app = FastAPI()
app.include_router(graphql_app, prefix="/graphql")  # new


# Test restful api
@app.get("/")
async def root():
    return {"message": "Hello World"}