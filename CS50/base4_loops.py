# ------------------------- while -------------------------
print("WHILE:::")
i = 3
while i > 0:
    print("meow")
    i -= 1


# ------------------------- for -------------------------
print("FOR:::")
for _ in range(3):
    print("meow")


# ------------------------- Pythonic -------------------------
print("PRINT (LOOP):::")
print("meow\n" * 3, end="")


# ------------------------- Checking user input infinitely ------------------------
print("CHECKING INPUT FOREVER:::")
while True:
    n = int(input("NUmber: "))
    if n > 0:
        break
for _ in range(n):
    print("meow")

# imprement modulality
print("MODULARITY:::")


def main():
    number = getNumber()
    meow(number)


def getNumber():
    while True:
        n = int(input("NUmber: "))
        if n > 0:
            return n


def meow(n):
    for _ in range(n):
        print("meow")


main()


# --------------------------------- Lists --------------------
print("LIST:::")
students = ["Kenny", "Maric", "Drick"]
for student in students:
    print(student)


# -----------------------------Dictionary--------------------
print("DICTIONARY:::")
student = {
    "name": "Kenny",
    "age": 19,
    "address": "KGL"
}
for info in student:
    print(student[info])

room = [
        {"id": 1, "name": "Kenny", "address": "KGL"},
        {"id": 2, "name": "mosses", "address": "KGL"}
]
for person in room:
    print(person["name"])
