#5. Quadratic Equation
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