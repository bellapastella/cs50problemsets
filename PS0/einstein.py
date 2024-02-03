def energy(mass):
  energy = mass * 300000000 ** 2
  return energy

mass = int(input("Provide a Mass: "))
print(energy(5))
