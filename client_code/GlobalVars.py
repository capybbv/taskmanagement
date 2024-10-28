import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

# users is a list of tuples: [(email, name), (email, name)...]
user_emails, user_colors = anvil.server.call("get_user_emails_and_colors")

column_types = ["Text", "Checkbox", "Priority", "Users", "Status"]

priority_items = ["Low", "Medium", "High"]

status_items = ["To do", "Doing", "Pending", "Done"]

priority_colors = {"Low": "#2DAF88", "Medium": "#F6CA57", "High": "#D64045"}

status_colors = {
  "To do": "#FFD700",
  "Doing": "#20B2AA",
  "Pending": "#FF0000",
  "Done": "#00FFFF",
}
