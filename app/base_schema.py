# strawberry/schema/base.py
from strawberry.schema import Schema
from strawberry.types import ExecutionContext
from graphql import GraphQLError

from strawberry.utils.logging import StrawberryLogger

from typing import List, Optional

class BaseSchema(Schema):
    def process_errors(
            self,
            errors: List[GraphQLError],
            execution_context: Optional[ExecutionContext] = None,
    ) -> None:
        for error in errors:
            return True