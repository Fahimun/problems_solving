# Python Program to Solve Quadratic Equation(দ্বিঘাত সমীকরণ সমাধানের জন্য পাইথন প্রোগ্রাম)

import cmath
def solve_quabratic_equation(a,b,c):
    delta = (b*2) - 4*(a*c)

    if delta >= 0:
        root1 = (-b + delta**0.5) / (2*a)
        root2 = (-b - delta**0.5) / (2*a)
        return root1, root2
    else:
        root1 = (-b + cmath.sqrt(delta) / (2*a) )
        root2 = (-b - cmath.sqrt(delta) / (2*a) )
        return root1, root2
    
a = 6
b = -8
c = 2

solutions = solve_quabratic_equation(a,b,c)

if isinstance(solutions,tuple):
    if solutions[0] == solutions[1]:
        print( f"The equation has a real seed: {solutions[0]}")
    else:
        print( f"The two real seeds of the equation are: {solutions[0]} and {solutions[1]}")


elif isinstance(solutions, complex):
  print(f"The two complex roots of the equation are: {solutions[0]} এবং {solutions[1]}")