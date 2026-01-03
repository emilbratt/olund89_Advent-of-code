f = open("2015_1.in")
r = f.read()

right = 0
left = 0
position = 1
for c in r:
    if c == "(":
        left = left + 1
    else:
        right = right + 1
    current = left - right
    if current == -1:
        break

    position = position + 1

p1 = left - right
print("Part 1 = " + str(p1))
print("Part 2 = " + str(p2))
