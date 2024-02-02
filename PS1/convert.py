def main():
  time = input("What time is it? ")
  converted_time = convert(time)

  if converted_time is None:
    return

  if 7 <= converted_time <= 8:
    print("breakfast time")
  elif 12 <= converted_time <= 13:
    print("lunch time")
  elif 18 <= converted_time <= 19:
    print("dinner time")
  else:
    return None

# 7:30 -> 7.5
def convert(time):
  hours, minutes = time.split(":")
  
  hours = int(hours)
  minutes = int(minutes) / 60

  valid = True
  if hours < 0 or hours > 23:
    print("Hours must be between 0 and 23.")
    valid = False

  if minutes < 0 or minutes >= 1:
    print("Minutes must be between 0 and 59.")
    valid = False

  if not valid:
    return None
  
  return float(hours + minutes)


main()