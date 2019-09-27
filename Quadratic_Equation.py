#5. Quadratic Equation
#Implement the function find_roots to find the roots of the quadratic equation: ax2 + bx + c = 0. 
#The function should return a tuple containing roots in any order.
def find_roots(a, b, c):
    riza = b**2 - 4*a*c
    riza = riza**(0.5)
    ThetikosArithmitis = -b + riza
    ArnitikoArithmitis = -b - riza
    sol1 = (ThetikosArithmitis/(2*a))
    sol2 = (ArnitikoArithmitis/(2*a))
    sol = (sol1, sol2)
    return sol

print(find_roots(2, 10, 8));
