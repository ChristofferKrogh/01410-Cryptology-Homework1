import itertools
import numpy as np

m = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
c = [1, 13, 8, 10, 4, 3, 0, 2, 15, 6, 14, 12, 5, 11, 7, 9]

S = [6, 4, 12, 5, 0, 7, 2, 14, 1, 15, 3, 13, 8, 10, 9, 11]
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

k3 = np.argmax(k3_counters)

z = [ciph ^ k3 for ciph in c]
y = [negS[element] for element in z]
# y corresponds to c in CipherTwo

k2_counters = np.zeros(16)
for m0, m1 in m_pairs:
    for k2_guess in range(16):
        c0 = y[m0]
        c1 = y[m1]
        x0 = c0 ^ k2_guess
        x1 = c1 ^ k2_guess
        if negS[x0] ^ negS[x1] == 13:
            k2_counters[k2_guess] += 1

k2 = np.argmax(k2_counters)

x = [element ^ k2 for element in y]
w = [negS[element] for element in x]
# w corresponds to c in CipherOne

k1_counters = np.zeros(16)
for m0, m1 in m_pairs:
    for k1_guess in range(16):
        c0 = w[m0]
        c1 = w[m1]
        v0 = c0 ^ k1_guess
        v1 = c1 ^ k1_guess
        if m0 ^ m1 == negS[v0] ^ negS[v1]:
            k1_counters[k1_guess] += 1

k1 = np.argmax(k1_counters)


u0 = negS[w[0] ^ k1]
k0 = m[0] ^ u0

print(f"k0: {k0}, k1: {k1}, k2: {k2}, k3: {k3}")

failure = False
for msg in m:
    ciph = S[S[S[msg ^ k0] ^k1] ^ k2] ^ k3
    failure = ciph != c[msg]

print(f"Fails? {failure}")


