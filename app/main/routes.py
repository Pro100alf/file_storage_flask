# from app.errors.handlers import
from typing import Optional

from flask import request
from flask_restx import Resource

from app.services.user import user_service, login_required
from app.services.file import file_service
from app.swagger import file_storage_api_ns, user_api_ns, swagger_models

@file_storage_api_ns.route('/upload', methods=['POST'])
class UploadController(Resource):

    @login_required
    @file_storage_api_ns.expect(swagger_models.request_file_upload_parser)
    @file_storage_api_ns.doc(security='basicAuth')
    @file_storage_api_ns.response(200, "Success", swagger_models.response_file_upload)
    @file_storage_api_ns.response(400, "BadRequest", swagger_models.response_user_not_found)
    @file_storage_api_ns.response(401, "Not Auth", swagger_models.response_auth_required)
    def post(self) -> dict:
        """Upload file file storage"""
        return file_service.upload_file()
    

@user_api_ns.route("", methods=['POST'])
class UserController(Resource):
    
    @user_api_ns.expect(swagger_models.request_user_create)
    @user_api_ns.response(200, "Success")
    @user_api_ns.response(400, "BadRequest", swagger_models.response_user_create_failed)
    def post(self) -> dict:
        return user_service.create_user()