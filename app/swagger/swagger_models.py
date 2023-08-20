from flask_restx import fields, reqparse
from werkzeug.datastructures import FileStorage

from app.swagger import file_storage_api_ns, user_api_ns

response_user_not_found = file_storage_api_ns.model('response_user_not_found', {
    'message': fields.String(example="User not found"),
})

response_auth_required = file_storage_api_ns.model('response_auth_required', {
    'message': fields.String(example="Authentication required"),
})

response_file_upload = file_storage_api_ns.model('response_file_upload', {
    'file_hash': fields.String(example="0a4d55a8d778e5022fab701977c5d840bbc486d0"),
})

request_user_create = user_api_ns.model('request_user_create', {
    'login': fields.String(example='user', required=True),
    'password': fields.String(example='password', required=True)
})

response_user_create_failed = user_api_ns.model('response_user_create_failed', {
    'message': fields.String(example='Login is already created')
})

request_file_upload_parser = reqparse.RequestParser()
request_file_upload_parser.add_argument('file', location='files', type=FileStorage, required=True)