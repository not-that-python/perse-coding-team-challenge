replies = ""
questions = ["how", "what", "why", "who", "when", "where"]

while True:
  message = input()
  
  if message == "goodbye":
    replies += "see you!"
    break

  message_list = message.split(" ")
  if message[-1] == "?":
    replies += "not sure really\n"
  elif message_list[0] in questions:
    replies += "not sure really\n"
  else:
    replies += "but why?\n"

print(replies)