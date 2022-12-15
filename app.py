from flask import Blueprint, Flask, request, jsonify
from flask_cors import CORS
import lib

base = Blueprint('base', __name__)


def create_app():
    application = Flask(__name__)
    application.register_blueprint(base)
    CORS(application)
    return application


@base.route('/')
def hello_world():
    return 'Hello World! Send a POST request to /alphabet-check to see a serverless API in action'


@base.route('/alphabet-check', methods=['POST'])
def alphabet_check():
    data = request.json
    result = lib.alphabet_check(data)
    return jsonify(result)


app = create_app()