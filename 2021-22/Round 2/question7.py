r_hop_len = int(input())
between_secs = int(input())
a_hop_len = int(input())


time = between_secs + 0
r_dist = r_hop_len * time
a_dist = 0
while True:
  time += 1
  r_dist += r_hop_len
  a_dist += a_hop_len
  if a_dist >= r_dist:
    break
print(time)