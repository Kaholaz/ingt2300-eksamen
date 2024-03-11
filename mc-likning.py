import sympy as sp

MC = sp.symbols("MC")
AC = sp.symbols("AC")
AC_der = sp.symbols("AC_der")
Q = sp.symbols("Q")

s = sp.solve(
    sp.Eq(MC, AC + Q * AC_der),
    [
        s
        for s in [MC, AC, AC_der, Q]
        if not (isinstance(s, int) or isinstance(s, float))
    ],
)

print(f"{s=}")
