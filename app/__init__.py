import logging
from flask import Flask

from app.config import Config


logger = logging.getLogger('file-storage')
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s %(levelname)s: %(message)s')
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    if app.debug:
        app.config['PROPAGATE_EXCEPTIONS'] = False
        

    from app.main import main_bp
    app.register_blueprint(main_bp)

    # from app.errors import bp as errors_bp
    # app.register_blueprint(errors_bp)

    from app.swagger import swagger_ui_blueprint
    app.register_blueprint(swagger_ui_blueprint)

    # from app.fixture import fixtures_blueprint
    # app.register_blueprint(fixtures_blueprint)

    # from app.decorators import log_first_request_info, log_request_info
    # app.before_request(log_request_info)
    # app.before_first_request(log_first_request_info)
    return app