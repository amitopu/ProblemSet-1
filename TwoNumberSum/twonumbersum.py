def twoNumberSum(array, targetSum):
    new_arr = []
    for i in range(0, len(array)-1): #iterate over 0th to n-1 th elem
        for j in range(i+1, len(array)): #iterate over i+1 th to n th elem
            if array[i] + array[j] == targetSum:
                new_arr.append(array[i])
                new_arr.append(array[j])
    if len(new_arr) != 0:
        return new_arr
    else:
        return False
    
    