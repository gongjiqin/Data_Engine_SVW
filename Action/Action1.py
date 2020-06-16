import numpy as np

s = 0
for n in range(2, 102, 2):
    s += n
print(s)

print(sum(range(2, 102, 2)))

a = np.arange(2, 102, 2)
print(sum(a))
