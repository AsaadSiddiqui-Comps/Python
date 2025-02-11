# NAME: Siddiqui Mohammed Asaad Shakir
#Roll no: 241258
#Branch:computer engineering   Batch: B3
#MModule 1
# PROGRAM NO 4
#Exploring Basic Arithmetic Operations in Python

def operation(num1, num2, function):
    if function == "+":
        return num1 + num2
    elif function == "-":
        return num1 - num2
    elif function == "*":
        return num1 * num2
    elif function == "/":
        if num2 != 0:
            return num1 / num2
        else:
            return "Cannot divide by zero"
    elif function == "%":
        return num1 % num2
    else:
        return "Invalid Choice"

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
function = input("Enter the Function (+, -, *, /, %): ")

result = operation(num1, num2, function)
print("Result:", result)
