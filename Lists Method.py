#Lists method
numbers = [1,2,3,4,5]
#add a number in list weuse append
numbers.append(6)
print(numbers)
#insert a number in list 
numbers.insert(0, -1)
print(numbers)
#removing a number in list
numbers.remove(3)
print(numbers)
#check items are exists in our list we use in operator
print(1 in numbers)
#check how many items are in the list
print(len(numbers))
#clear list
numbers.clear()
print(numbers)
