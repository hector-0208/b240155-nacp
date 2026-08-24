x = 5
t = (1, 2, 3, 4)
# t = tuple(list(t[:1]) + [x] + list(t[2:]))
t = tuple([x] + list(t[1:]))
print(t)
a = 13
b = 11
t = tuple(list(t[:1]) + [a, b] + list(t[3:]))
print(t)
t = (1, 2, 3, 4)
z = 15
t = (t[0], z, *t[2:])
print(t)

x = (1, -1)
d = (3, 2)
temp = list(d)
temp[0] = 1
d = tuple(temp)
print(type(d))
print(d)
X = x + d
print(f"\n{X}")

