num= int(input("enter a number to be checked: ")) # program to check whether the entered number is prime or not.

if num==1:
    print("It is not a prime number")

if num>1:
    for i in range(2,num):
        if num % i ==0:
            print("It is not a prime number")
            break

        else:
            print("It is a prime number")