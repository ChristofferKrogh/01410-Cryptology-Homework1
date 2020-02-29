import numpy as np
import itertools

S = [6, 4, 12, 5, 0, 7, 2, 14, 1, 15, 3, 13, 8, 10, 9, 11]
negS = [4, 8, 6, 10, 1, 3, 0, 5, 12, 14, 13, 15, 2, 11, 7, 9]

m = [1, 14, 2, 13, 3, 12]
c = [15, 8, 7, 11, 6, 10]

def find_pairs_with_diff(list, difference = 15):
    m_pairs = []
    for m0, m1 in itertools.combinations(list, 2):
        if m0 ^ m1 == difference:
            m_pairs.append((m0, m1))
    return m_pairs

def find_k2(m_pairs, cipher_dict):
    k2_counters = np.zeros(16)
    for m0, m1 in m_pairs:
        for k2_guess in range(16):
            c0 = cipher_dict[m0]
            c1 = cipher_dict[m1]
            x0 = c0 ^ k2_guess
            x1 = c1 ^ k2_guess
            if negS[x0] ^ negS[x1] == 13:
                k2_counters[k2_guess] += 1
    print(f"k2 counters:\n{k2_counters}")
    return np.argmax(k2_counters)

def find_k1(m_pairs, cipher_dict):
    k1_counters = np.zeros(16)
    for m0, m1 in m_pairs:
        for k1_guess in range(16):
            c0 = cipher_dict[m0]
            c1 = cipher_dict[m1]
            v0 = c0 ^ k1_guess
            v1 = c1 ^ k1_guess
            if m0 ^ m1 == negS[v0] ^ negS[v1]:
                k1_counters[k1_guess] += 1
    print(f"k1 counters:\n{k1_counters}")
    return np.argmax(k1_counters)

def check_key_validity(keys):
    valid = True
    for idx, msg in enumerate(m):
        ciph = S[S[msg ^ keys[0]] ^keys[1]] ^ keys[2]
        valid = ciph == c[idx]
        if not valid:
            break

    return valid

def main():
    m_pairs = find_pairs_with_diff(m, 15)
    c_dict = {}
    for idx, msg in enumerate(m):
        c_dict[msg] = c[idx]
    k2 = find_k2(m_pairs, c_dict)

    x = [k2 ^ e for e in c]
    w = [negS[e] for e in x]
    w_dict = {}
    for idx, msg in enumerate(m):
        w_dict[msg] = w[idx]
    # w corresponds to c in CipherOne
    k1 = find_k1(m_pairs, w_dict)

    u0 = negS[w[0] ^ k1]
    k0 = m[0] ^ u0

    print(f"k0: {k0}, k1: {k1}, k2: {k2}")
    valid = check_key_validity([k0, k1, k2])
    print(f"Valid? {valid}")

if __name__ == '__main__':
    main()