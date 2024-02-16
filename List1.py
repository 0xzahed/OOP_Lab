  
Newlist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

Odd = []
Even = []

for num in Newlist:
    if num % 2 == 0:
        Even.append(num)
    else:
        Odd.append(num)

print("Odd numbers:", Odd)
print("Even numbers:", Even)
