import os

desktop_path = os.path.expanduser("~/Desktop")
downloads_path = os.path.expanduser("~/Downloads")
documents_path = os.path.expanduser("~/Documents")

# for file_name in os.listdir(downloads_path):
#   file_path = os.path.join(downloads_path, file_name)
#   if os.path.isfile(file_path):
#     size = os.path.getsize(file_path)
#     print(f"File: {file_name}, Size: {size} bytes")

# for file in os.listdir(downloads_path):
#   if file.endswith(".svg"):
#     print(f"Danh sach file svg o downloads: {file}")

# for file_name in os.listdir(documents_path):
#   file_path = os.path.join(documents_path, file_name)
#   if os.path.isfile(file_path):
#     size = os.path.getsize(file_path)/1024
#     if size > 10:
#       print(f"File: {file_name}, Size: {size} KB")
#   if not os.path.isfile(file_path):
#     print(f"File: {file_name} is not a file")
#   if os.path.isdir(file_path):
#     print(f"File: {file_name} is a directory")

for file_name in os.listdir(downloads_path):
  file_path = os.path.join(downloads_path, file_name)
  if os.path.isfile(file_path):
    open("log.txt", "w").write(f"{file_name}\n")
  




  