from flask import Flask
from api import api_bp


def create_app(config_filename):
    application = Flask(__name__)
    application.config.from_object(config_filename)
    
    application.register_blueprint(api_bp, url_prefix='/api')

    return application


application = create_app("config")	
if __name__ == "__main__":
    #application = create_app("config")
    application.run(host='0.0.0.0', port=5090, debug=True)