# from app.errors.handlers import
from typing import Optional

from app.swagger import file_storage_api_ns
# from app import swagger_models, services
from flask_restx import Resource

@file_storage_api_ns.route('/<string:subject_id>/sleep/stages', methods=['POST'])
class SleepDataController(Resource):

    @file_storage_api_ns.doc(security='basic', params={"subject_id": "subject id ('000TEST')"})
    # @file_storage_api_ns.response(200, "Success", swagger_models.sleep_response)
    # @file_storage_api_ns.response(400, "BadRequest", swagger_models.response_user_not_found)
    # @file_storage_api_ns.doc(body=swagger_models.data_fields)
    def post(self, subject_id: Optional[str] = None) -> dict:
        """Get sleep data (raw, smooth, table)"""
        # return services.post_sleep_stages(subject_id)