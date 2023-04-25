from flask import Blueprint, jsonify

healthcheck = Blueprint('healthcheck', __name__)
readiness = Blueprint('readiness', __name__)

@healthcheck.route('/health')
def health():
    return jsonify({'status': 'OK'})

@readiness.route('/ready')
def readiness():
    return jsonify({'status': 'OK'})
