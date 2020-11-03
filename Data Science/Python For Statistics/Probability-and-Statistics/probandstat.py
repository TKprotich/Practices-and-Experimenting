# Import sympy and FiniteRV 
from sympy.stats import P, E, variance, Die, Normal
from sympy import Eq, simplify
import sympy
a, b, k = sympy.symbols('a b k')

X, Y = Die('X', 3), Die('Y', 6) # two six sided dice

Z = Normal('Z',  0, 1) # Declare a Normal random variable with mean 0, and std 1

a = 0*k + k + 2*k + 3*k + k*k + 2*k*k + 7*k*k +k

b = simplify(a-1)
print(b)
