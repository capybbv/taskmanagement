import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from anvil import *
import anvil.js

base_url = "https://automatic-golden-candle.anvil.app/_/api/abc"


def startup():
  user = anvil.users.login_with_form()
  if not user["color"]:
    anvil.server.call("add_user_color")
  open_form("Frame")


startup()

try:
  response = anvil.server.call("abc_api")
  # response = anvil.http.request(base_url, method="GET")
  print(response)
except Exception as e:
  print(e)
