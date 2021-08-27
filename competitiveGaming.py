# def solution(k, scores):
#     if(k <= 0 ):
#         return 0
#     rank = 1
#     res = 0
#     scores.sort()
#     for idx in range(0, len(scores)):
#         if (idx == 0):
#             rank = 1
#         elif (scores[idx] != scores[idx-1]):
#             rank = idx + 1
#         if(rank <= k and scores[idx] > 0):
#             res += 1
#         else:
#             break
#     return res

# print(solution(4, [2, 2, 3, 4, 5]))

# def solution2(A, B, P):
#     found = []
#     subString = str(P)
#     # write your code in Python 3.6
#     for idx in range(len(B)):
#         if (B[idx].find(subString) == -1):
#             continue
#         else:
#             found.append(A[idx])
#     if len(found) > 0:
#         found.sort()
#         return found[0]
#     else:
#         return 'NO CONTACT'
#     pass

# A = ['sander', 'amy', 'ann', 'micheal']
# B = ['123456789', '234567890', '789123456', '123123123']
# P = 1

# print(solution2(A, B, P))

import re
def solution3(S):
    # write your code in Python 3.6
    if len(S) < 2:
        raise Exception("S should have a lenth greather than 3")
    
    cleanS = re.sub('[^0-9a-zA-Z]+', '', S)
    results = '-'.join(cleanS[i:i+3] for i in range(0, len(cleanS), 3))
    if (len(cleanS) % 3 != 1) :
        return results
    else:
        return results
    pass

print(solution3('00-44 48 5555 8361'))
print(solution3('555372654'))
print(solution3('0 - 22 1985--324'))