def Even_Number(Num1, Num2):
    Number = []
    for num in range(Num1, Num2 + 1):
        if num % 2 == 0:
            Number.append(num)
    return Number

A = int(input("Enter number: "))
B = int(input("Enter number: "))

Even = Even_Number(A, B)
print("Even numbers: ", A, "and", B, "are:", Even)
