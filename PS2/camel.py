camel = input("Provide a camel case name: ")
snake = ""

for letter in camel:
  if letter.islower():
    snake += letter
  else:
    snake += "_" + letter.lower()

print(snake)