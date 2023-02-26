no_votes = int(input())

scores = {}

for i in range(no_votes):
  vote = input()
  name1, name2_n_choice = vote.split(":")
  choice, name2 = name2_n_choice.split(" ")
  if name1 not in scores.keys():
    scores[name1] = 0
  if name2 not in scores.keys():
    scores[name2] = 0
  scores[name2] += (1 if choice == "UP" else -1)

smallest = min(scores.values())
kicked_off = []
for name in scores:

  if scores[name] == smallest:
    kicked_off.append(name)

kicked_off.sort()

for name in kicked_off:
  print(name)
