import anvil.google.auth, anvil.google.drive, anvil.google.mail
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
from . import ColumnModule
from . import RowsModule


@anvil.server.callable(require_user=True)
def add_project_to_table(project_name):
  project_row = app_tables.projects.add_row(project_name=project_name)
  project_row["columns"] = []

  # init the table with predefined columns
  ColumnModule.add_column_to_db("Task Name", project_row, "Text")
  ColumnModule.add_column_to_db("Priority", project_row, "Priority")
  ColumnModule.add_column_to_db("Done", project_row, "Checkbox")

  # add an empty row to new project
  row_data = {row.get_id(): "" for row in project_row["columns"]}
  RowsModule.add_row_to_rows(project_row, row_data)
  return project_row


@anvil.server.callable(require_user=True)
def get_projects():
  return app_tables.projects.search()


@anvil.server.callable(require_user=True)
def change_project_name(row, new_name):
  row["project_name"] = new_name
  row["project_name"] = row["project_name"]


@anvil.server.callable(require_user=True)
def delete_project(project_row):
  if project_row is not None:
    for col in project_row["columns"]:
      # delete the columns in the columns data table
      col.delete()
    for row in app_tables.rows.search(project=project_row):
      # delete the rows in the rows data table
      row.delete()
    # delete the actual project row
    project_row.delete()
