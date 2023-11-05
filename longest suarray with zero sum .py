#logest array with sum 0 #




'''
    Time Complexity: O(N), where 'N' is the length of 'Arr'.

    Space Complexity: O(N), where 'N' is the length of 'Arr'.
'''
from typing import *

def getLongestZeroSumSubarrayLength(arr : List[int]) -> int:

    n = len(arr)
    prefix_sum, ans = 0, 0

    # The hashmap to store the first index at which a prefix sum occurs.
    first_index = {}

    first_index[0] = -1

    # Traversing through the array.
    for i in range(n):
        prefix_sum += arr[i]

        # Finding the longest length subarray ending at 'i' and having zero-sum.
        if prefix_sum in first_index:
            ans = max(ans, i - first_index[prefix_sum])
        else:
            first_index[prefix_sum] = i

    return ans