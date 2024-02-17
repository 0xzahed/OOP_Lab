List = [1, 2, 3, 4, 5]

print("Create list:", List)

List[2] = 10
print("List after changing item at index 2:", List)

List.append(6)
print("List after adding item:", List)

List.remove(4) 
print("List after removing item with value 4:", List)


List.sort()
print("Sorted list:", List)
