import re
from datetime import datetime
import logging

logging.basicConfig(filename='validation_errors.log', level=logging.ERROR)

def validate_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email) is not None

def validate_timestamp(timestamp):
    try:
        datetime.fromisoformat(timestamp.replace('Z', '+00:00'))
        return True
    except ValueError:
        return False

def validate_task(task):
    if not isinstance(task, dict):
        return False, "Task must be a dictionary"
    
    if 'task_id' not in task or not isinstance(task['task_id'], str) or task['task_id'] == "":
        return False, "task_id must be a non-empty string"
    
    if 'completed' not in task or not isinstance(task['completed'], bool):
        return False, "completed must be a boolean"
    
    if 'description' in task and not isinstance(task['description'], str):
        return False, "description must be a string if provided"
    
    return True, ""

def validate_data(data):
    errors = []

    if 'user_id' not in data or not isinstance(data['user_id'], str) or data['user_id'] == "":
        errors.append("user_id must be a non-empty string")

    if 'email' not in data or not validate_email(data['email']):
        errors.append("Invalid email format")

    if 'timestamp' not in data or not validate_timestamp(data['timestamp']):
        errors.append("Invalid timestamp format. Must be ISO 8601 with timezone")

    if 'tasks' not in data or not isinstance(data['tasks'], list) or len(data['tasks']) == 0:
        errors.append("tasks must be a non-empty list of dictionaries")
    else:
        for i, task in enumerate(data['tasks']):
            is_valid, task_error = validate_task(task)
            if not is_valid:
                errors.append(f"Invalid task at index {i}: {task_error}")

    if errors:
        for error in errors:
            logging.error(error)
        return False, errors

    return True, []