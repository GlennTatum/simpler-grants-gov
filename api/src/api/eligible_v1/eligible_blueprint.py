from apiflask import APIBlueprint

eligible_blueprint = APIBlueprint(
    "eligible_v1",
    __name__,
    tag="Eligible v1",
    url_prefix="/v1",
)
