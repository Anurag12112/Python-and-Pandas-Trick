#taking input from user first number and we canpass our string to our float function for type conversion
first = float(input("First: "))
#taking input from user second number
second = float(input("Second: "))
# for addition we use sum
sum =first+second
#call str function because python doesn't know how to concatenate float to string so we need to covert sum into string
print("Sum: " + str(sum))