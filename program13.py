#to vheck whether it is valid triangle or not
a= int(input("Enter the first side: "))
b= int(input("Enter the second side: "))
c= int(input("Enter the third side:  "))

if a+b>c or b+c>a or c+a>b: # sum of two sides of triangle is greater than the first
    print("it is a vaid triangle")

else:
    print("It is not a triangle")