import sympy as sp

Q = sp.symbols("Q")
P = # Sett inn uttrykk
TC = P * Q
TC_der = sp.diff(TC, Q)
q = sp.solve(sp.Eq(TC_der, 0), Q)[0]
print(f"{q=}")
p = P.evalf(subs={Q: q})
print(f"{p=}")
