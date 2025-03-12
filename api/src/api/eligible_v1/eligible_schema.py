from src.api.schemas.extension import Schema, fields
from src.api.schemas.response_schema import AbstractResponseSchema, PaginationMixinSchema
from src.pagination.pagination_schema import generate_pagination_schema


class EligibleRequestSchema(Schema):
    pass

class EligibleResponseSchema(Schema):
    description = fields.String()

class EligibleListReponseSchema(Schema):
    data = fields.List(
        fields.Nested(EligibleResponseSchema),
        metadata={"description": "list of eligible organizations"}
    )