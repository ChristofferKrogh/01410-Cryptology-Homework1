m = [1, 14, 2, 13, 3, 12]
c = [15, 8, 7, 11, 6, 10]

S = [6, 4, 12, 5, 0, 7, 2, 14, 1, 15, 3, 13, 8, 10, 9, 11]
negS = [4, 8, 6, 10, 1, 3, 0, 5, 12, 14, 13, 15, 2, 11, 7, 9]

k2 = -1
k1 = -1

for i in range(16):
    diff1 = negS[i ^ c[0]] ^ negS[i ^ c[1]]
    diff2 = negS[i ^ c[2]] ^ negS[i ^ c[3]]
    diff3 = negS[i ^ c[4]] ^ negS[i ^ c[5]]
    if diff1 == 13 and diff2 == 13 and diff3 == 13:
        k2 = i

w = [negS[k2 ^ e] for e in c]

for i in range(16):
    u_diff1 = negS[w[0] ^ i] ^ negS[w[1] ^ i]
    u_diff2 = negS[w[2] ^ i] ^ negS[w[3] ^ i]
    u_diff3 = negS[w[4] ^ i] ^ negS[w[5] ^ i]
    if u_diff1 == 15 and u_diff2 == 15 and u_diff3 == 15:
        k1 = i
        break

u = [negS[k1 ^ e] for e in w]

k0 = m[0] ^ u[0]

print(f"keys.\nk0 = {k0}, k1 = {k1}, k2 = {k2}")

for i, msg in enumerate(m):
    ciph = S[S[msg ^ k0] ^ k1] ^ k2
    print(ciph, c[i])
    if ciph != c[i]:
        print("Something happened")


