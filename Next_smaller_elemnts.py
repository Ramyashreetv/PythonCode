#The idea is to find the Next Smaller Element for each array element one by one. To find the Next Smaller for an array element we will start moving to the right of that element and will try to find the first element having a value smaller than that element and set the Next Smaller Element as that element and end our search. If we reach the end of the array without finding any such element then we will set the next smaller element as -1 for that element.

Let ans be an array of length N that stores the Next Smaller Elements.#
'''
    Time Complexity: O(N ^ 2)
    Space Complexity: O(1)

    Where N denotes the number of elements in the array.
'''

def nextSmallerElement(arr, n):

    # Defining the list to store next smaller elements for the array.
    ans = [0 for i in range(n)]

    # Iterating through all the array elements and finding next smaller element for each element.
    for i in range(n):

        # Initializing the next smaller element as -1.
        ans[i] = -1

        # Moving to the right of the element.
        for j in range(i + 1, n):

            # Checking for the next smaller element.
            if(arr[i] > arr[j]):
                ans[i] = arr[j]
                break

    # Returning the final vector after all the iterations
    return ans
