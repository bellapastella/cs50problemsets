text = input("Provide text: ")
output = ""
for letter in text:
  vowels = ["a", "e", "i", "o", "u"]
  if letter.lower() not in vowels:
    output += letter

print(output)