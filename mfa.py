import numpy as np

A = np.array(
    [
        # Definer likningene
    ]
)
if len(A) == 0:
    raise ValueError("Likningene er ikke deinert.")
if A.shape[0] != A.shape[1]:
    raise ValueError("Du har ikke definert nok likninger (A må være kvadratisk)")

# Definer konstanter i likningene
y = np.zeros(len(A))
y.reshape((A.shape[0], 1))

x = np.linalg.solve(A, y)
print(f"{x=}")
