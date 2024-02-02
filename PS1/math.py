def get_math(math):
  x, y, z = math.split(" ")

  x, z = float(x), float(z)
  
  if y == "+":
    return x + z
  elif y == "-":
    return x - z
  elif y == "*":
    return x * z
  elif y == "/":
    return x / z
  else:
    return None

math = input("Please provide a math expression: ")
print(get_math(math))
