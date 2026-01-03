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

print("current = " + str(current) + " position = " + str(position))
    

p1 = left - right
print("Part 1 = " + str(p1))