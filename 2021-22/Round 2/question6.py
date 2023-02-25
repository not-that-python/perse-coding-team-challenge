# Obtaining the input
width = int(input())
height = int(input())
grid = []

for _ in range(height):
  grid_row = [int(i) for i in list(input())]
  grid.append(grid_row)

  
# Splitting up the grid
middle_width = int(width / 2)
middle_height = int(height / 2)

top = grid[:middle_height]
top_left = []
top_right = []
for row in range(len(top)):

  top_left.append(top[row][:middle_width])
  top_right.append(top[row][middle_width:])

bottom = grid[middle_height:]
bottom_left = []
bottom_right = []
for row in range(len(bottom)):

  bottom_left.append(bottom[row][:middle_width])
  bottom_right.append(bottom[row][middle_width:])


# Multiplying them together
final_overlay = []

for i in range(middle_height):
  final_overlay.append([])
  for j in range(middle_width):
    final_overlay[i].append(top_left[i][j] * top_right[i][j] *
                            bottom_left[i][j] * bottom_right[i][j])


# Counting up the 1s
count = 0
for i in range(len(final_overlay)):
  for j in range(len(final_overlay[i])):
    if final_overlay[i][j]:
      count += 1
print(count)
