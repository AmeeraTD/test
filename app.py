from flask import Flask, request, jsonify
from validation import validate_data;
from authorization import require_api_token;
from data_processing import process_tasks;
from pagination import paginate_tasks;


app = Flask(__name__)

@app.route('/submit', methods=['POST'])
@require_api_token
def submit():
    data = request.json
    is_valid, errors = validate_data(data)
    
    if not is_valid:
        return jsonify({"errors": errors}), 400
    

        # Process the valid data here
    summary = process_tasks(data['tasks'])
    return jsonify({"message": "Data submitted successfully", "summary": summary}), 200

@app.route('/tasks', methods=['GET'])
def get_tasks():
    data = request.json
    tasks = data['tasks']
    
    page_size = int(request.args.get('page_size', 10))
    page_number = int(request.args.get('page', 1))
    
    paginated_result = paginate_tasks(tasks, page_size, page_number)
    
    return jsonify(paginated_result), 200


if __name__ == '__main__':
    app.run(debug=True, port=8080)