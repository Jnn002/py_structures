""" 
# Time Complexity: O(n^2)
# Space Complexity: O(1)
def two_sum_brute_force(A, target):
    for i in range(len(A)-1):
        for j in range(i+1, len(A)):
            if A[i] + A[j] == target:
                print(F'Valor i: {A[i]}, valor j: {A[j]}')
                return True
    return False

A = [-2, 1, 2, 4, 7, 11]
target = 8
print(two_sum_brute_force(A,target), '\n')
target = 20
print(two_sum_brute_force(A,target)) 
"""

# Time Complexity: O(n)
# Space Complexity: O(1)
def two_sum(A, target):
    i = 0
    j = len(A) - 1
    while i < j:
        if A[i] + A[j] == target:
            print(A[i], A[j])
            return True
        elif A[i] + A[j] < target:
            i += 1
        else:
            j -= 1
    return False

A = [-2, 1, 2, 4, 7, 11]
target = 13

print(two_sum(A,target))