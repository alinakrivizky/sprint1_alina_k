new_tasks = ['task_001', 'task_011', 'task_007', 'task_015', 'task_005']
completed_tasks = ['task_002', 'task_012', 'task_006'] 

new_tasks.remove('task_005')
completed_tasks.append('task_005')
new_tasks.remove('task_007')

print('New tasks:', new_tasks)
print('Completed tasks:', completed_tasks)
new_tasks.reverse()
tasks_by_priority = new_tasks
print(tasks_by_priority[0])