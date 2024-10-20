num= int(input("Enter a number which is to be checked: "))

if num>=0 and num<=9:
    print("It is a single digit number")

elif num>=10 and num<=99:
    print("It is a two digit number") 

else:
    print("Please enter a valid number")