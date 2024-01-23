import numpy as np

with open('input.txt', 'r') as file:
    n = int(file.readline().strip())
    A = np.array([list(map(float, file.readline().split())) for _ in range(n)])
    B = np.array([list(map(float, file.readline().split())) for _ in range(n)])
    I = np.identity(n)

mas = []
for i in range(len(A)):
    mas.extend(np.roots([-1, A[i][i]]))

print(round(min(mas), 4))
