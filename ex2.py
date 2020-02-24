import itertools
import numpy as np

m = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
c = [1, 13, 8, 10, 4, 3, 0, 2, 15, 6, 14, 12, 5, 11, 7, 9]

negS = [4, 8, 6, 10, 1, 3, 0, 5, 12, 14, 13, 15, 2, 11, 7, 9]

m_pairs = []
for m0, m1 in itertools.combinations(m, 2):
    if m0 ^ m1 == 15:
        m_pairs.append((m0, m1))

k3_counters = np.zeros(16)
for m0, m1 in m_pairs:
    for k3_guess in range(16):
        c0 = c[m0]
        c1 = c[m1]
        z0 = c0 ^ k3_guess
        z1 = c1 ^ k3_guess
        if negS[z0] ^ negS[z1] == 12:
            k3_counters[k3_guess] += 1

print(f"counters for k3: {k3_counters}")
print(f"k3 = {np.argmax(k3_counters)}")


