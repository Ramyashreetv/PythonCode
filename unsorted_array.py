

#Kth largest element in the unsorted array#


'''
	Time Complexity: O(K + (N - K) * log(K))
    Space Complexity: O(K)

    where N is the length of the array and K is order of the largest element to be found.
'''

from sys import stdin, stdout
import heapq


def kthLargest(arr, size, k):
    # pq will be used as a priority queue.
    pq = [] 

    for i in range(size):
        if i < k:
            # All heap related operations are performed using inbuilt heappq library.
            heapq.heappush(pq, arr[i]) 

        else:
            val = pq[0]
            if val < arr[i]:
                heapq.heappop(pq)
                heapq.heappush(pq, arr[i])

    return pq[0]




































'''
	Time Complexity: O(K + (N - K) * log(K))
    Space Complexity: O(K)

    where N is the length of the array and K is order of the largest element to be found.
'''

from sys import stdin, stdout
import heapq


def kthLargest(arr, size, k):
    # pq will be used as a priority queue.
    pq = [] 

    for i in range(size):
        if i < k:
            # All heap related operations are performed using inbuilt heappq library.
            heapq.heappush(pq, arr[i]) 

        else:
            val = pq[0]
            if val < arr[i]:
                heapq.heappop(pq)
                heapq.heappush(pq, arr[i])

    return pq[0]



































