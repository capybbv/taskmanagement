import anvil.google.auth, anvil.google.drive, anvil.google.mail
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server


# @anvil.server.callable(require_user=True)
# def get_columns(project):
#   return app_tables.projects.search(project=project)


@anvil.server.callable(require_user=True)
def add_column_to_db(column_name, project, type):
  column_row = app_tables.columns.add_row(title=column_name, type=type)
  project["columns"] += [column_row]
  return column_row


@anvil.server.callable(require_user=True)
def change_column_title(column_id, new_title):
  app_tables.columns.get(id=column_id)["title"] = new_title


@anvil.server.callable(require_user=True)
def delete_column(row, project):
  # row is a row from the columns data table
  if row is not None:
    # remove columns from project data table
    columns = project["columns"]
    columns.remove(row)
    project["columns"] = columns
    # remove from columns data table
    row.delete()


@anvil.server.callable(require_user=True)
@anvil.server.callable(anvil.server.http_endpoint("/"))
def get_column_types():
  return app_tables.types.search()
