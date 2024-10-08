from z3 import *

solver = Solver()

s = [BitVec(f's{i}', 8) for i in range(41)]

solver.add((((s[0] + s[1]) & 255) + s[2]) & 255 == 44)
solver.add((((s[1] - s[2]) & 255) + s[3]) & 255 == 54)
solver.add((((s[2] + s[3]) & 255) + s[4]) & 255 == 122)
solver.add((((s[3] + s[4]) & 255) - s[5]) & 255 == 47)
solver.add((((s[4] + s[5]) & 255) - s[6]) & 255 == 90)
solver.add((((s[5] - s[6]) & 255) - s[7]) & 255 == 13)
solver.add((((s[6] - s[7]) & 255) - s[8]) & 255 == 99)
solver.add((((s[7] - s[8]) & 255) - s[9]) & 255 == 9)
solver.add((((s[8] - s[9]) & 255) - s[10]) & 255 == 244)
solver.add((((s[9] + s[10]) & 255) - s[11]) & 255 == 143)
solver.add((((s[10] + s[11]) & 255) + s[12]) & 255 == 140)
solver.add((((s[11] + s[12]) & 255) + s[13]) & 255 == 52)
solver.add((((s[12] - s[13]) & 255) - s[14]) & 255 == 27)
solver.add((((s[13] + s[14]) & 255) + s[15]) & 255 == 88)
solver.add((((s[14] - s[15]) & 255) + s[16]) & 255 == 154)
solver.add((((s[15] - s[16]) & 255) + s[17]) & 255 == 135)
solver.add((((s[16] - s[17]) & 255) + s[18]) & 255 == 77)
solver.add((((s[17] - s[18]) & 255) - s[19]) & 255 == 78)
solver.add((((s[18] - s[19]) & 255) - s[20]) & 255 == 159)
solver.add((((s[19] + s[20]) & 255) - s[21]) & 255 == 9)
solver.add((((s[20] + s[21]) & 255) + s[22]) & 255 == 233)
solver.add((((s[21] + s[22]) & 255) + s[23]) & 255 == 143)
solver.add((((s[22] - s[23]) & 255) - s[24]) & 255 == 179)
solver.add((((s[23] + s[24]) & 255) + s[25]) & 255 == 194)
solver.add((((s[24] + s[25]) & 255) - s[26]) & 255 == 18)
solver.add((((s[25] - s[26]) & 255) - s[27]) & 255 == 25)
solver.add((((s[26] - s[27]) & 255) + s[28]) & 255 == 225)
solver.add((((s[27] + s[28]) & 255) + s[29]) & 255 == 203)
solver.add((((s[28] - s[29]) & 255) + s[30]) & 255 == 71)
solver.add((((s[29] - s[30]) & 255) - s[31]) & 255 == 20)
solver.add((((s[30] + s[31]) & 255) - s[32]) & 255 == 11)
solver.add((((s[31] + s[32]) & 255) + s[33]) & 255 == 101)
solver.add((((s[32] - s[33]) & 255) - s[34]) & 255 == 71)
solver.add((((s[33] - s[34]) & 255) - s[35]) & 255 == 11)
solver.add((((s[34] + s[35]) & 255) - s[36]) & 255 == 74)
solver.add((((s[35] - s[36]) & 255) - s[37]) & 255 == 243)
solver.add((((s[36] + s[37]) & 255) + s[38]) & 255 == 177)
solver.add((((s[37] + s[38]) & 255) + s[39]) & 255 == 60)
solver.add((((s[38] - s[39]) & 255) + s[40]) & 255 == 204)

if solver.check() == sat:
    model = solver.model()
    solution = [model[s[i]].as_long() for i in range(41)]
    print("Solution found:")
    #print(solution)

else:
    print("No solution found")

xor_key = [140, 98, 22, 87,105,
           114, 185, 15, 86, 46,
           30, 211, 207, 174, 147, 
           232, 231, 28, 60, 127,
           13, 67, 37, 106, 109,
           70, 230, 205, 208, 56,
           29, 138, 140, 229, 200,
           244, 13, 4, 179, 122, 48]

flag = [solution[i] ^ xor_key[i] for i in range(41)]
flag = [flag[i] ^ 77 for i in range(41)]
print(''.join([chr(flag[i]) for i in range(41)]))
