from functools import wraps
from flask import request, jsonify

# Authorization
API_TOKENS = {
    "valid-api-token": "user123",
    "sasika123":"sasika"
}

def require_api_token(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth_header = request.headers.get('Authorization')
        if not auth_header or not auth_header.startswith('Bearer '):
            return jsonify({"error": "Invalid or missing Authorization header"}), 401
        
        token = auth_header.split(' ')[1]
        if token not in API_TOKENS:
            return jsonify({"error": "Invalid API token"}), 401
        
        return f(*args, **kwargs)
    return decorated