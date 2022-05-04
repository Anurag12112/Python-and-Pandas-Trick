weight = int(input("Weight"))#int is using because it can not multiply sequence of character by int #weight variable is containing string
unit = input("(K)g or (L)bs: ")
if unit.upper() == "K": #conver this string in upper case
    converted = weight / 0.45 #converting weight in pounds
    print("Weight in Lbs: "+ str(converted))
else:
    converted = weight * 0.45
    print("weight in kgs: " +str(converted)) #use str because python can only concatenate stringvnot ("float")
