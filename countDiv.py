#### Problem ####
#### Write a function:
# 
# def solution(A, B, K)
# 
# that, given three integers A, B and K, returns the number of integers within the range [A..B] that are divisible by K, i.e.:
# 
# { i : A ≤ i ≤ B, i mod K = 0 }
# 
# For example, for A = 6, B = 11 and K = 2, your function should return 3, because there are three numbers divisible by 2 within the range [6..11], namely 6, 8 and 10.
# 
# Write an efficient algorithm for the following assumptions:
# 
# A and B are integers within the range [0..2,000,000,000];
# K is an integer within the range [1..2,000,000,000];
# A ≤ B.

def solution(A, B, K):
    if B < A or K <= 0:
        raise Exception("Invalid Input")
 
    min_value =  ((A + K -1) // K) * K
 
    if min_value > B:
      return 0
 
    return ((B - min_value) // K) + 1

print(solution(1, 10, 2))