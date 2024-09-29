import math

def paginate_tasks(tasks, page_size, page_number):
    total_tasks = len(tasks)
    total_pages = math.ceil(total_tasks / page_size)
    
    start_index = (page_number - 1) * page_size
    end_index = start_index + page_size
    
    paginated_tasks = tasks[start_index:end_index]
    
    return {
        "tasks": paginated_tasks,
        "page_size": page_size,
        "page_number": page_number,
        "total_pages": total_pages
    }
