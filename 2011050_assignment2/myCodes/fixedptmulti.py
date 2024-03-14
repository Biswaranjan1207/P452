import pandas as pd

xtable = [[1.5, 3.5]]
ErrorTable = [1]
Nmax = 100
eps = 0.000001
i = 1

while ErrorTable[i - 1] > eps and i <= Nmax:
    x1new = (10 - xtable[i - 1][0] * xtable[i - 1][1]) ** 0.5
    x2new = ((57 - xtable[i - 1][1]) / 3 / x1new) ** 0.5
    xnew = [x1new, x2new]
    xtable.append(xnew)
    
    er = sum((a - b) ** 2 for a, b in zip(xnew, xtable[i - 1])) ** 0.5 / sum(a ** 2 for a in xnew) ** 0.5
    ErrorTable.append(er)
    i += 1

T2 = [[j + 1, xtable[j][0], xtable[j][1], xtable[j + 1][0], xtable[j + 1][1], ErrorTable[j + 1]] for j in range(len(xtable) - 1)]

df = pd.DataFrame(T2, columns=["Iteration", "x1_in", "x2_in", "x1_out", "x2_out", "Er"])
print(df)
