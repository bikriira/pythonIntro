"""
    marks checker: this will explain if..elif..else
"""
def main():
    marks = int(input("Marks: "))
    print(isEven(marks))
    if marks >= 90 and marks <= 100:
        print("A")
    if marks >= 80 and marks < 90:
        print("B")
    if marks >= 70 and marks < 80:
        print("C")
    if marks >= 60 and marks < 70:
        print("D")
    if marks >= 50 and marks < 60:
        print("F")
    if marks < 50:
        print("Fail")

    #    | Simplify |
    
    marks = int(input("Marks: "))
    print(isEven(marks))
    if 90 <= marks <= 100:
        print("A")
    if 80 <= marks < 90:
        print("B")
    if 70 <= marks < 80:
        print("C")
    if 60 <= marks < 70:
        print("D")
    if 50 <= marks < 60:
        print("F")
    if marks < 50:
        print("Fail")

    #   | simplify |

    marks = int(input("Marks: "))
    print(isEven(marks))
    if 90 <= marks:
        print("A")
    elif 80 <= marks:
        print("B")
    elif 70 <= marks:
        print("C")
    elif 60 <= marks:
        print("D")
    elif 50 <= marks:
        print("F")
    elif marks < 50:
        print("Fail")

    name = input("Name: ")
    match name:
        case "Sing" | "Encanto" | "Luca": # this means if "sing" 0r "encanto" ...
            print("Cartoon name")
        case "Peter rabbit":
            print("Not a cartoon name")
        case _:
            print("Unkown name")

def isEven(number):
    return True if number % 2 == 0 else False

    #   | Simplify |
    return number % 2 == 0


main()