import anvil.google.auth, anvil.google.drive, anvil.google.mail
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

# This is a server module. It runs on the Anvil server,
# rather than in the user's browser.
#
# To allow anvil.server.call() to call functions here, we mark
# them with @anvil.server.callable.
# Here is an example - you can replace it with your own:
#
# @anvil.server.callable
# def say_hello(name):
#   print("Hello, " + name + "!")
#   return 42
#
@anvil.server.callable
def add(a, b):
    return a + b


@anvil.server.callable
def add_task(project, title, priority, status, estimate, created_by):
    return app_tables.tasks.add_row(project=project,
                                    title=title,
                                    priority=priority,
                                    status=status,
                                    estimate=estimate,
                                    created_at=anvil.server.call('anvil.server.datetime.now'),
                                    created_by=created_by)

@anvil.server.callable
def get_tasks_1():
    return app_tables.tasks.search()

@anvil.server.callable
@anvil.server.http_endpoint("/tasks/{task_id}")
def get_task_by_id(task_id):
    return app_tables.tasks.get(task_id=task_id)

@anvil.server.callable
def update_task(task_id, **kwargs):
    task = app_tables.tasks.get(task_id=task_id)
    task.update(**kwargs)
    task.updated_at = anvil.server.call('anvil.server.datetime.now')
    return task

@anvil.server.callable
def delete_task(task_id):
    task = app_tables.tasks.get(task_id=task_id)
    task.delete()
    return task
  
