a = input("enter your name:")
print("Welcome",str(a))


# Program make a simple calculator

# This function adds two numbers
def add(x, y):
    return x + y

# This function subtracts two numbers
def subtract(x, y):
    return x - y

# This function multiplies two nuMilmbers
def multiply(x, y):
    return x * y

# This function divides two numbers
def divide(x, y):
    return x / y


print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

while True:
    # Take input from the user
    yourchoice = input("Enter choice(1/2/3/4): ")

    # Check if choice is one of the four options
    if yourchoice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if yourchoice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif yourchoice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif yourchoice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif yourchoice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
        break
    else:
        print("Invalid Input")
print("Thanks for using basic calculator")