import random as rand, statistics as stat, sys


for _ in range(5):
    nomine = ["one", "two", "three"]
    rand.shuffle(nomine) # modifies the passed original sequence
    print(rand.choice(nomine))
    print(rand.randint(0, 3))

print(stat.mean([80, 70]))

if len(sys.argv) < 2:
    print("Few arguments")

for arg in sys.argv[1:]:
    print(arg)