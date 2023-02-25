num1 = int(input())
num2 = int(input())

possible = []
if num1 <= 20:
  # try num1 as pounds
  num1 = str(num1)
  num2 = str(num2)

  if len(num2) == 1:
    num2 = "0" + num2

  possible.append(f"£{num1}.{num2}")
num1 = int(num1)
num2 = int(num2)

if num2 <= 20:
  # try num2 as pounds
  num1 = str(num1)
  num2 = str(num2)

  if len(num1) == 1:
    num1 = "0" + num1

  possible.append(f"£{num2}.{num1}")
num1 = int(num1)
num2 = int(num2)

if len(possible) == 1:
  print(possible[0])
else:

  if possible[0] == possible[1]:
    print(possible[0])

  elif num1 < num2:
    print(possible[0])
    print(possible[1])
  else:
    print(possible[1])
    print(possible[0])
