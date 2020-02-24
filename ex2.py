import itertools
import numpy as np

m = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
c = [1, 13, 8, 10, 4, 3, 0, 2, 15, 6, 14, 12, 5, 11, 7, 9]

S = [6, 4, 12, 5, 0, 7, 2, 14, 1, 15, 3, 13, 8, 10, 9, 11]
negS = [4, 8, 6, 10, 1, 3, 0, 5, 12, 14, 13, 15, 2, 11, 7, 9]

def find_pairs_with_diff(list, difference = 15):
    m_pairs = []
    for m0, m1 in itertools.combinations(list, 2):
        if m0 ^ m1 == difference:
            m_pairs.append((m0, m1))
    return m_pairs

def find_key_from_ciphertext(m_pairs, ciphertexts, difference):
    counters = np.zeros(16)
    for m0, m1 in m_pairs:
        for key_guess in range(16):
            c0 = ciphertexts[m0]
            c1 = ciphertexts[m1]
            z0 = c0 ^ key_guess
            z1 = c1 ^ key_guess
            if negS[z0] ^ negS[z1] == difference:
                counters[key_guess] += 1

    return np.argmax(counters)

def find_k1_from_ciphertext(m_pairs, ciphertexts):
    k1_counters = np.zeros(16)
    for m0, m1 in m_pairs:
        for k1_guess in range(16):
            c0 = ciphertexts[m0]
            c1 = ciphertexts[m1]
            v0 = c0 ^ k1_guess
            v1 = c1 ^ k1_guess
            if m0 ^ m1 == negS[v0] ^ negS[v1]:
                k1_counters[k1_guess] += 1

    return np.argmax(k1_counters)

def check_key_validity(keys):
    valid = True
    for msg in m:
        ciph = S[S[S[msg ^ keys[0]] ^keys[1]] ^ keys[2]] ^ keys[3]
        valid = ciph == c[msg]
        if not valid:
            break

    return valid

def main():
    m_pairs = find_pairs_with_diff(m, 15)
    k3 = find_key_from_ciphertext(m_pairs, c, 12)

    z = [ciph ^ k3 for ciph in c]
    y = [negS[element] for element in z]
    # y corresponds to c in CipherTwo
    k2 = find_key_from_ciphertext(m_pairs, y, 13)

    x = [element ^ k2 for element in y]
    w = [negS[element] for element in x]
    # w corresponds to c in CipherOne
    k1 = find_k1_from_ciphertext(m_pairs, w)

    u0 = negS[w[0] ^ k1]
    k0 = m[0] ^ u0

    print(f"k0: {k0}, k1: {k1}, k2: {k2}, k3: {k3}")
    valid = check_key_validity([k0, k1, k2, k3])
    print(f"Valid? {valid}")
    

if __name__ == '__main__':
    main()