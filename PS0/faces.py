def convert(str):
  str = str.replace(":)", "🙂")
  str = str.replace(":(", "🙁")
  return str

str = input("Please enter a string: ")
output = convert(str)
print(output)
