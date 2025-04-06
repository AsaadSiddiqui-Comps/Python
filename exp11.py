a = int(float(input("Enter first number: "))) 
b = int(float(input("Enter second number: ")))

print("Addition of two numbers is: ", a+b)
print("Subtraction of two numbers is: ", a-b)
print("Multiplication of two numbers is: ", a*b)

if b!= 0:
    print("Division of two numbers is: ", a/b)
else:
    print(f"Division Answer is Infinity Because Denominator is Zero:- {a}/{b}")


a = int(input("Enter first number: "))) 
b = int(input("Enter second number: ")))
    # Check if the first number is even or odd
    if a % 2 == 0:
        print(f"The first number {a} is Even.")
    else:
        print(f"The first number {a} is Odd.")