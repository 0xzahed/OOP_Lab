
New_Tuple = (1,2,3,4,5,6)
print("Item:",New_Tuple)

print("Access Item :",New_Tuple[2])
x = list(New_Tuple)
x[1] = "33"
New_Tuple = tuple(x)

print("Add New Item",New_Tuple) 
