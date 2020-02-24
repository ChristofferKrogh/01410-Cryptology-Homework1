import numpy as np

ddt = np.zeros((16, 16))
# ddt[0,0] = 16
ddt[1] =  [0, 0, 6, 0, 0, 0, 0, 2, 0, 2, 0, 0, 2, 0, 4, 0]
ddt[2] =  [0, 6, 6, 0 ,0 ,0 ,0 ,0 ,0, 2, 2, 0, 0, 0, 0, 0]
ddt[3] =  [0, 0, 0, 6, 0, 2, 0, 0, 2, 0, 0, 0, 4, 0, 2, 0]
ddt[4] =  [0, 0, 0, 2, 0, 2, 4, 0, 0, 2, 2, 2, 0, 0, 2, 0]
ddt[5] =  [0, 2, 2, 0, 4, 0, 0, 4, 2, 0, 0, 2, 0, 0, 0, 0]
ddt[6] =  [0, 0, 2, 0, 4, 0, 0, 2, 2, 0, 2, 2, 2, 0, 0, 0]
ddt[7] =  [0, 0, 0, 0, 0, 4, 4, 0, 2, 2, 2, 2, 0, 0, 0, 0]
ddt[8] =  [0, 0, 0, 0, 0, 2, 0, 2, 4, 0, 0, 4, 0, 2, 0, 2]
ddt[9] =  [0, 2, 0, 0, 0, 2, 2, 2, 0, 4, 2, 0, 0, 0, 0, 2]
ddt[10] = [0, 0, 0, 0, 2, 2, 0, 0, 0, 4, 4, 0, 2, 2, 0, 0]
ddt[11] = [0, 0, 0, 2, 2, 0, 2, 2, 2, 0, 0, 4, 0, 0, 2, 0]
ddt[12] = [0, 4, 0, 2, 0, 2, 0, 0, 2, 0, 0, 0, 0, 0, 6, 0]
ddt[13] = [0, 0, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 6, 2, 0, 4]
ddt[14] = [0, 2, 0, 4, 2, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 6]
ddt[15] = [0, 0, 0, 0, 2, 0, 2, 0, 0, 0, 0, 0, 0, 10, 0, 2]

best_two_rounds = []
for row in ddt:
    row_max = max(row)
    idx = np.where(row == row_max)[0]
    two_round_max = 0
    for i in idx:
        if max(ddt[i]) > two_round_max:
            two_round_max = max(ddt[i])

    print(row_max, two_round_max)
    best_two_rounds.append(row_max / 16 * two_round_max / 16)

print(f"Probabilities: {best_two_rounds}")
print(f"Highest Probability: {max(best_two_rounds)}")
    
