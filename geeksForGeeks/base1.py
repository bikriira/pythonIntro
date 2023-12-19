# Python Datatypes and Declaration
"""
    In this section i'm going to cover python datatypes, declaration 
    and initialisation.
"""

myVariable = "string"
print(myVariable)

myVariable = 4
print(myVariable)

myVariable = 4.2
print(myVariable)

itemsMix = []
itemsMix = [1, 2.5, "Banana", [1, "apple"]]
print(itemsMix)
itemsMix.append("Mango")
print(itemsMix)


# Input and Output
"""
    In this section i'm going to cover how to input user data and 
    then print them.
"""

name = input("Enter your name here: ")
print("Your name is: ", name)

# Selection / condition statements

print("Simple calculator:")
num1 = int(input("Enter First number: "))
operation = input("Choose between '+' and '-': ")
num2 = int(input("Enter second number: "))

if operation == "+":
    print("The sum is: ", num1 + num2)
elif operation == "-":
    print("The difference is :", num1 - num2)
else:
    print("Invalid operation")

# My first function


def write(string):
    print(string)


write("Hello this is my first function")


"""
    The Main() function will only be triggered if the script is 
    executed as the main program, not when the script is imported as a module
    into another script.
"""


def Main():
    print("Inside Main function")


if __name__ == "__main__":
    Main()