import sympy as sp

# Define variable
x = sp.Symbol('x')

# Define function
f = sp.sin(x) + x**2

# Perform indefinite integration
indef_integral = sp.integrate(f, x)

print("f(x) =", f)
print("∫f(x) dx =", indef_integral)