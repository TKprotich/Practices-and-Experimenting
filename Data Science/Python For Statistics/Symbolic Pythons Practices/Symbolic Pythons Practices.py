Python 3.7.6 (default, Jan  8 2020, 20:23:39) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> """ Symbolic Computation"""
' Symbolic Computation'
>>> import math
>>> import sympy
>>> math.sqrt(1.2)
1.0954451150103321
>>> sympy.sqrt(1.2)
1.09544511501033
>>> sympy.sqrt(2)
sqrt(2)
>>> sympy.sqrt(1.5)
1.22474487139159
>>> sympy.sqrt(4)
2
>>> sympy.sqrt(9)
3
>>> sympy.sqrt(8)
2*sqrt(2)
>>> """ The exact sqrt of eight is 2*sqrt(2)"""
' The exact sqrt of eight is 2*sqrt(2)'
>>> sympy.sqrt(3)
sqrt(3)
>>> sympy.sqrt(3.5)
1.87082869338697
>>> """ This is the power of symbolic computation """
' This is the power of symbolic computation '
>>> """ sympy is capable of computing symbolic expressions with variables.
The variables are defined using `symbols` and they are defined before they are used"""
' sympy is capable of computing symbolic expressions with variables.\nThe variables are defined using `symbols` and they are defined before they are used'
>>> x, y = sympy.symols('x y')
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    x, y = sympy.symols('x y')
AttributeError: module 'sympy' has no attribute 'symols'
>>> x, y = sympy.symbols('x y')
>>> expr = x + 2*y
>>> expr
x + 2*y
>>> expr + 2
x + 2*y + 2
>>> "play with it"
'play with it'
>>> expr*3
3*x + 6*y
>>> expr^3
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    expr^3
TypeError: unsupported operand type(s) for ^: 'Add' and 'int'
>>> " You can't do power"
" You can't do power"
>>> expr-3
x + 2*y - 3
>>> expr1 = expr +7
>>> expr2 = expr1 + expr
>>> expr2
2*x + 4*y + 7
>>> expr3 = expr2*5 + expr1*100 + expr
>>> expr3
111*x + 222*y + 735
>>> x*expr3
x*(111*x + 222*y + 735)
>>> expr3 - 222*y
111*x + 735
>>> expr3 - 222*y + 111*x
222*x + 735
>>> x*(expr3 - 222*y + 111*x)
x*(222*x + 735)
>>> """ Symbolic python can:
1. Simplify expressions.
2. Compute derivatives, integrals and limits.
3. solve equations.
4. Work with matrices.
----It has modules for plotting, printing, code generation, pysics, statistics, combonatorics, number theory, geometry, logic and more---
"""
' Symbolic python can:\n1. Simplify expressions.\n2. Compute derivatives, integrals and limits.\n3. solve equations.\n4. Work with matrices.\n----It has modules for plotting, printing, code generation, pysics, statistics, combonatorics, number theory, geometry, logic and more---\n'
>>> 