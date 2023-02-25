outside = int(input())
inside = int(input())
out_chr = input()
in_chr = input()

top_n_bottom = outside * out_chr

inside_space = outside - 2
spaces = int((inside_space - inside) / 2)

middle = out_chr + (" "*spaces) + (in_chr*inside) + (" "*spaces) + out_chr

top_n_middle = None
if spaces != 0:
  top_n_middle = out_chr + (" "*inside_space) + out_chr


print(top_n_bottom)

for _ in range(spaces):
  print(top_n_middle)

for _ in range(inside):
  print(middle)

for _ in range(spaces):
  print(top_n_middle)
  
print(top_n_bottom)