import numpy as np

A = np.array(
    [
        # Definer inn teknologimatrise
    ]
)
if len(A) == 0:
    raise ValueError("Teknologimatrise er ikke definert.")

f = np.array(
    [
        # Definer sluttforbruksvektoren
    ]
)
if len(f) == 0:
    raise ValueError("Sluttforbruksvektoren er ikke definert.")

B = np.array(
    [
        # Definer inversjonsmatrisa
    ]
)
if len(B) == 0:
    raise ValueError("Inversjonsmatrisa er ikke definert.")

s = np.linalg.solve(A, f)
print(f"{s=}")

r = B @ s
print(f"{r=}")
