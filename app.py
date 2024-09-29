from flask import Flask, request, jsonify
from validation import validate_data;


app = Flask(__name__)

@app.route('/submit', methods=['POST'])
def submit():
    data = request.json
    is_valid, errors = validate_data(data)
    
    if not is_valid:
        return jsonify({"errors": errors}), 400
    

    return jsonify({"message": "Data is Valid"}), 200


if __name__ == '__main__':
    app.run(debug=True, port=8080)