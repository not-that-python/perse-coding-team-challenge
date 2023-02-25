actual_weight = float(input())

rounded_weight = ((actual_weight // 50) + 1) * 50
leftover = round((rounded_weight - actual_weight), 1)

print(leftover)