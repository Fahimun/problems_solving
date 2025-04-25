import cmath
a = 2
b = 3
c = 5


delta = (b**2) - (4 * a*c)

ans1 = (-b - cmath.sqrt(delta))/(2 * a)
ans2 = (-b + cmath.sqrt(delta))/( 2 * a)

print(ans1)
print(ans2)