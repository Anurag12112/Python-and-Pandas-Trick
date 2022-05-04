#Tuples arekind of lists to store a sequence of object but #tuples are immutable
#tuples doesn't assign new value or add and remove values
#a tuples is similar to a list except tuples are immutable;we cannot change elemnts of tuple
numbers = (1,2,3,4) #use parenthesis to define tuple

for number in numbers:
    print(number)
#join two tuples
tuple1 = ('cat','dog','horse')
tuple2 = (1,2,3)
tuple_join = tuple1 + tuple2
print(tuple_join)
