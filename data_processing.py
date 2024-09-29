def process_tasks(tasks):
    total_tasks = len(tasks)
    completed_tasks = sum(1 for task in tasks if task['completed'])
    
    return {
        "total_tasks": total_tasks,
        "completed_tasks": completed_tasks
    }