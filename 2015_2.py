f = open("2015_2.in")
lines = f.read().splitlines()

p1 = 0
p2 = 0
for line in lines:
    s = line.split("x")
    l = int(s[0])
    w = int(s[1])
    h = int(s[2])
    bow = l*w*h

    arr = [l, w, h]
    arr.sort()
    a, b = arr[0], arr[1]
    ribbon = a*2 + b*2

    x = l*w
    y = w*h
    z = l*h
    surface = (2*x) + (2*y) + (2*z)
    ll = [x,y,z]
    slack = min(ll)
    paper = surface + slack
    p1 += paper
    p2 += (ribbon + bow)


print("Part 1 =", p1)
print("Part 2 =", p2)
