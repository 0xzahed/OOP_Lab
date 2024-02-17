NewList = []

n = int(input("Enter the number of elements you want to add to the list: "))
for n in range(n):
    item = input("Enter an item: ")
    NewList.append(item)

print("Initial list:", NewList)

if NewList:
    index = int(input("Enter the index of the item you want to change: "))
    if index < len(NewList):
        new_value = input("Enter the new value: ")
        NewList[index] = new_value
        print("List after changing item:", NewList)
    else:
        print("Index out of range.")
else:
    print("List is empty.")

new_item = input("Enter an item to add to the list: ")
NewList.append(new_item)
print("List after adding item:", NewList)


if NewList:
    remove_item = input("Enter an item to remove from the list: ")
    if remove_item in NewList:
        NewList.remove(remove_item)
        print("List after removing item:", NewList)
    else:
        print("Item not found in the list.")
else:
    print("List is empty.")


print("Looping through the list:")
for item in NewList:
    print(item)


NewList.sort()
print("Sorted list:", NewList)
