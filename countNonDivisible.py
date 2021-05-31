#### Problem ####
# You are given an array A consisting of N integers.
# 
# For each number A[i] such that 0 ≤ i < N, we want to count the number of elements of the array that are not the divisors of A[i]. We say that these elements are non-divisors.
# 
# For example, consider integer N = 5 and array A such that:
# 
#     A[0] = 3
#     A[1] = 1
#     A[2] = 2
#     A[3] = 3
#     A[4] = 6
# For the following elements:
# 
# A[0] = 3, the non-divisors are: 2, 6,
# A[1] = 1, the non-divisors are: 3, 2, 3, 6,
# A[2] = 2, the non-divisors are: 3, 3, 6,
# A[3] = 3, the non-divisors are: 2, 6,
# A[4] = 6, there aren't any non-divisors.
#### Write a function:
# 
# def solution(A)
# 
# that, given an array A consisting of N integers, returns a sequence of integers representing the amount of non-divisors.
# 
# Result array should be returned as an array of integers.
# 
# For example, given:
# 
#     A[0] = 3
#     A[1] = 1
#     A[2] = 2
#     A[3] = 3
#     A[4] = 6
# the function should return [2, 4, 3, 2, 0], as explained above.
# 
# Write an efficient algorithm for the following assumptions:
# 
# N is an integer within the range [1..50,000];
# each element of array A is an integer within the range [1..2 * N].

def solution(A):
  
    A_max = max(A)
  
    count = {}
    for element in A:
        if element not in count:
            count[element] = 1
        else:
            count[element] += 1
  
    divisors = {}
    for element in A:
        divisors[element] = set([1, element])
  
    # start the Sieve of Eratosthenes
    divisor = 2
    while divisor*divisor <= A_max:
        element_candidate = divisor
        while element_candidate  <= A_max:
            if element_candidate in divisors and not divisor in divisors[element_candidate]:
                divisors[element_candidate].add(divisor)
                divisors[element_candidate].add(element_candidate//divisor)
            element_candidate += divisor
        divisor += 1
  
    result = [0] * len(A)
    for idx, element in enumerate(A):
        result[idx] = (len(A)-sum([count.get(divisor,0) for divisor in divisors[element]]))
  
    return result

print(solution([3, 1, 2, 3, 6]))