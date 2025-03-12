import uuid
from datetime import date
from typing import TYPE_CHECKING

import src.adapters.db as db
import src.adapters.db.flask_db as flask_db
import src.api.response as response
from src.auth.api_key_auth import api_key_auth
import src.api.eligible_v1.eligible_schema as eligible_schema

from sqlalchemy import select
from src.db.models.lookup_models import LkApplicantType

from src.api.eligible_v1.eligible_blueprint import eligible_blueprint 

@eligible_blueprint.post("/eligible_applicants")
@eligible_blueprint.output(eligible_schema.EligibleListReponseSchema)
@eligible_blueprint.auth_required(api_key_auth)
@flask_db.with_db_session()
def eligible_get(db_session: db.Session) -> response.ApiResponse:

    # Call service with params to get results
    with db_session.begin():
        stmt = select(LkApplicantType)
    
    result = db_session.scalars(stmt).all()
    
    as_json = [{"description": item.description} for item in result]

    # mock = [{"description": "school"}]

    # Serialize results
    return response.ApiResponse(message="Success", data=as_json)