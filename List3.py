List = [5, 3, 9, 2, 7, 1]

max = List[0]
min = List[0]

for num in List:
    if num > max:
        max = num
    elif num < min:
        min = num

print("Maximum Number:", max)
print("Minimum Number:", min)
