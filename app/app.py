from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter
from app.base_schema import BaseSchema
# GraphQL Core
from app.modules.core import Query, Mutation
# Develop
# schema = strawberry.Schema(query=Query, mutation=Mutation)
# Production
schema = BaseSchema(query=Query, mutation=Mutation)
graphql_app = GraphQLRouter(schema)
# Start fastapi and include modules to the router
app = FastAPI()
app.include_router(graphql_app, prefix="/api")  # new
# Test Restful api
@app.get("/")
async def root():
    return {"message": "Hello World"}