user_fruit = input("Please provide a fruit: ").lower()

fruits = {"apple": 130, "avocado": 50, "sweet cherries": 100}

if user_fruit in fruits:
  print("Calories:", fruits[user_fruit])
else:
  print("That's not a fruit.")
