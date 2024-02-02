def get_media_type(file):
  split_file = file.split(".")
  # hello.png -> ["hello", "png"]

  # return if the file does not have an extension
  if len(split_file) == 1:
    return "application/octet-stream"

  # the text after the last period is the file extension
  ext = split_file[-1]

  # swap out any "jpg" with "jpeg"
  if ext == "jpg":
    ext = "jpeg"

  # Return the proper file extension
  if ext == "gif" or ext == "png" or ext == "jpeg":
    return "image/" + ext
  else:
    return "application/octet-stream"

# get the user's input file name
file = input("What's the name of the file? ").lower().strip()

file_type = get_media_type(file)
print(file_type)