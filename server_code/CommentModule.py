import anvil.google.auth, anvil.google.drive, anvil.google.mail
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server


@anvil.server.callable(require_user=True)
def get_comments(project):
  return app_tables.comments.search(project=project)


@anvil.server.callable(require_user=True)
def add_comment(comment, project):
  app_tables.comments.add_row(
    comment=comment, user=anvil.users.get_user(), project=project
  )


@anvil.server.callable(require_user=True)
def delete_comment(row):
  if row is not None:
    row.delete()
