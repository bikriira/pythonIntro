def main():
    num1 = float(input("First num: "))
    num2 = float(input("Second num: "))
    print(num1 / num2)
    print(round(3.14659, 2))  # or print(f"{3.14659:.2f}) # outputs 3.15
    print(f"{1000:,}")  # otputs 1,000
    name = "Bikri"
    greating1 = hello()
    greating2 = hello(name)
    print(greating1 + "\n" + greating2)


def hello(name="world"):  # name by default is world
    return f"Hello, {name}"


"""
    In order to call the function before definning it, we can use this tactic:
        - main function holds the main code,
        - main function is called at the end to ensure that every thing have been deined before
"""
main()
