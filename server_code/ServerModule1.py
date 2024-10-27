import anvil.google.auth, anvil.google.drive, anvil.google.mail
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import anvil.http


USER_COLORS = [
  "Primary",
  "Secondary",
  "Tertiary",
  "Primary Container",
  "On Secondary Container",
]


@anvil.server.callable(require_user=True)
def change_cell_value(row, column_id, new_text):
  row["data"] = {**row["data"], column_id: new_text}


@anvil.server.callable(require_user=True)
def add_user_color():
  user_row = anvil.users.get_user()
  num_of_users = len(app_tables.users.search())
  user_row["color"] = USER_COLORS[num_of_users % 5]


@anvil.server.callable(require_user=True)
def get_user_emails_and_colors():
  users = app_tables.users.search()
  emails = [user["email"] for user in users]
  colors = {user["email"]: f"theme:{user['color']}" for user in users}
  return emails, colors


@anvil.server.callable
def get_tasks():
  tasks = []
  for row in app_tables.tasks.search():
    task_data = {
      "id": row.get_id(),
      "name": row["name"],
      "status": row["status"],
      "created_at": row["created_at"],
    }
    tasks.append(task_data)
  return tasks


@anvil.server.http_endpoint("/abc", methods=["GET"])
def abc_api():
  try:
    print("Endpoint /abc has been called")
    data = anvil.server.request.query_params.get("data")
    if data:
      print(f"Data received: {data}")
      return f"Received data: {data}"
    else:
      # Giả sử ở đây bạn muốn trả về tất cả dữ liệu khi không có tham số `data`
      all_data = {"od": "123123123"}  # Hàm này sẽ trả về tất cả dữ liệu bạn cần
      print("Returning all data")
      return all_data
  except Exception as e:
    print(f"Error occurred: {str(e)}")
    return anvil.server.HttpResponse(500, f"Internal Server Error: {str(e)}")
