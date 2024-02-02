import string

def main():
  plate = input("Plate: ")
  if is_valid(plate):
    print("Valid")
  else:
    print("Invalid")


def is_valid(s):
  # check for proper length
  if len(s) < 2 or len(s) > 6:
    print("Must be between 2 and 6 characters!")
    return False

  # check if first two characters are letters
  if not s[0:1].isalpha():
    print("First two characters must be letters!")
    return False
  
  # check for any punctuation marks
  for character in s:
    if character in string.punctuation or character.isspace():
      print("There cannot be any spaces or punctuation marks!")
      return False

  # check that numbers are at the end
  number_found = False
  for character in s:
    if character == "0" and not number_found:
      print("The first number can not be 0.")
      return False
    elif character.isnumeric():
      number_found = True
    elif number_found and character.isalpha():
      print("Numbers cannot be used in the middle.")
      return False

  return True


main()