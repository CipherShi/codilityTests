#### Problem ####
#### Write a function
# 
# def solution(A)
# 
# that, given an array A consisting of N integers, returns the number of distinct values in array A.
# 
# For example, given array A consisting of six elements such that:
# 
#  A[0] = 2    A[1] = 1    A[2] = 1
#  A[3] = 2    A[4] = 3    A[5] = 1
# the function should return 3, because there are 3 distinct values appearing in array A, namely 1, 2 and 3.
# 
# Write an efficient algorithm for the following assumptions:
# 
# N is an integer within the range [0..100,000];
# each element of array A is an integer within the range [−1,000,000..1,000,000].

# solution #1
# def solution(A):
#     if len(A) == 0:
#         return 0
 
#     A.sort()
 
#     nr_values = 1
#     last_value = A[0]
 
#     for idx in range(1, len(A)):
#         if A[idx] != last_value:
#             nr_values += 1
#             last_value = A[idx]
 
#     return nr_values

# solution #2
def solution(A):
    return len(set(A))

print(solution([2, 1, 1, 2, 3, 1]))

