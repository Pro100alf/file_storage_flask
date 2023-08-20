from flask import Blueprint
from flask_restx import Api
import os
import datetime


swagger_ui_blueprint = Blueprint("/", __name__)
authorizations = {
    'basicAuth': {
        'type': 'basic',
        'in': 'header',
        'name': 'Authorization'
    }
}
file_storage_api = Api(swagger_ui_blueprint,
               doc='/swagger',
               catch_all_404s=True,
               title='File Storage Service',
               description="Test file storage service",
               authorizations=authorizations
               )
file_storage_api_ns = file_storage_api.namespace('/', description='REST API file storage')
