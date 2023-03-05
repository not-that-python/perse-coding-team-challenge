queue = list(map(int, input()))


def median(nums):
  sort_nums = sorted(nums)
  middle = round(len(sort_nums) / 2 + 0.1) - 1
  return sort_nums[middle]


room = []
for i in range(len(queue)):
  result = median(queue[:i + 1])
  room.append(result)

print(''.join(list(map(str, room))))
