you are given a singly linked list of array B of size N .each elemnt in the array B represtens a block of code . modifiy the linked list by revering nodesin each black whoes size aregiven bythe array B
''' 

    Time Complexity : O(L)
    Space Complexity : O(L / K)
    
    Where L is the number of nodes in the Linked-List.
    Where K is the minimum block size from the array B.

'''

# List Node Class.
class Node:
    def __init__(self, data):

        self.data = data
        self.next = None


def reverseKElements(head, n, b, idx):

    # Base case: List is empty or entire block array have been considered.
    if (head == None or idx >= n):
        return head

    # K is the size of the current block.
    K = b[idx]

    # Just move to the next block if size of the current block is zero.
    if (K == 0):
        return reverseKElements(head, n, b, idx + 1)

    cur = head
    prev = None
    ahead = None

    # Variable to keep track of the number of nodes reversed in the current block.
    cnt = 0

    # Reverse nodes until end of list is reached or current block has been reversed.
    while (cur != None and cnt < K):
        ahead = cur.next
        cnt += 1
        cur.next = prev
        prev = cur
        cur = ahead

    # Reverse the next block.
    head.next = reverseKElements(ahead, n, b, idx + 1)
    return prev


def getListAfterReverseOperation(head, n, b):

    # If linked list is empty, return head of the linked list.
    if (head == None):
        return head

    # Calling reverseKElements function to modify the given linked list.
    head = reverseKElements(head, n, b, 0)

    # Return the head of the linked list.
    return head