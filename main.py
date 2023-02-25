a = int(input())
b = int(input())
c = int(input())

phrase = ""
if (a**2) + (b**2) == c**2:
  phrase = "equal to"
elif (a**2) + (b**2) < c**2:
  phrase = "less than"
else:
  phrase = "greater than"

print(f"{a} squared plus {b} squared is {phrase} {c} squared")