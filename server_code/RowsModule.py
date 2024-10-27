import anvil.google.auth, anvil.google.drive, anvil.google.mail
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server


@anvil.server.callable(require_user=True)
def get_rows(project):
  return app_tables.rows.search(project=project)


@anvil.server.callable(require_user=True)
def add_row_to_rows(project, row_data):
  app_tables.rows.add_row(project=project, data=row_data)


@anvil.server.callable(require_user=True)
def delete_row(row):
  if row is not None:
    row.delete()
