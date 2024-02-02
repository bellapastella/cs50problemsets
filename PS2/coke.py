cents = 0

while cents < 50:
  print("You owe", 50-cents, "cents.")
  coin = int(input("Insert Coin: "))
  if coin == 25 or coin == 10 or coin == 5:
    cents += coin
  else:
    print("Coin not accepted.")

print("Change amount:", cents-50)