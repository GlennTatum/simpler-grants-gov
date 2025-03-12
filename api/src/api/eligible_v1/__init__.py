from src.api.eligible_v1.eligible_blueprint import eligible_blueprint

# import agency_routes module to register the API routes on the blueprint
import src.api.eligible_v1.eligible_routes # noqa: F401 E402 isort:skip

__all__ = ["eligible_blueprint"]
