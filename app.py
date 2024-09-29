from flask import Flask, request, jsonify
from data_processing import process_tasks;
from validation import validate_data;
from authorization import require_api_token;
from pagination import paginate_tasks;

app = Flask(__name__)

@app.route('/submit', methods=['POST'])
def submit():
    data = request.json
    is_valid, errors = validate_data(data)
    
    if not is_valid:
        return jsonify({"errors": errors}), 400
    
    # Process the valid data here
    summary = process_tasks(data['tasks'])
    return jsonify({"message": "Data submitted successfully", "summary": summary}), 200


if __name__ == '__main__':
    app.run(debug=True, port=8080)