#Valid Pairing of Numbers#
'''
	Time complexity: O(N)
	Space complexity: O(N)
	
	Where 'N' is the length of the given array.
'''
    
def minSwaps(arr, n):
    
    #  HashMap to store the number along with their position as they present in the given list/array.
    mp = dict()
    
    for i in range(2 * n):
        mp[arr[i]] = i
        
    # Variable to store the minimum number of swaps needed to make valid pairing of numbers.
    count = 0
    
    # Iterate through "arr".
    for i in range(0, 2 * n, 2):
        # Variable to store the other number to which arr[i] should be paired.
        num = 0
        
        if arr[i] % 2 == 0:
            num = arr[i] + 1
            
        else:
            num = arr[i] - 1
            
        # Check if arr[i] is already in the valid pairing then continue the iterations.
        if arr[i + 1] == num:
            continue
        
        # Otherwise, swap the required numbers to make valid pairing of numbers.
        temp = arr[i + 1]
        
        arr[i + 1] = arr[mp[num]]
        
        arr[mp[num]] = temp
        
        mp[arr[mp[num]]] = mp[num]
        
        # Also, increment the "count" by 1.
        count = count + 1
        
    return count