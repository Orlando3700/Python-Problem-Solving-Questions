# Merge Sort without Recursion
# Since Merge Sort is a divide and conquer algorithm,
# recursion is the most intuitive code to use for
# implementation. The recursive implementation of Merge
# Sort is also perhaps easier to understand, and uses less
# code lines in general.

# But Merge Sort can also be implemented without the use
# of recursion, so that there is no function calling itself.

def merge(left, right):
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
            
    result.extend(left[i:])
    result.extend(right[j:])
    
    return result

def mergeSort(arr):
    step = 1  # Starting with sub-arrays of length 1
    length = len(arr)
    
    while step < length:
        for i in range(0, length, 2 * step):
            left = arr[i:i + step]
            right = arr[i + step:i + 2 * step]
            
            merged = merge(left, right)
            
            # Place the merged array back into the original array
            for j, val in enumerate(merged):
                arr[i + j] = val
                
        step *= 2  # Double the sub-array length for the next iteration
        
    return arr

unsortedArr = [3, 7, 6, -10, 15, 23.5, 55, -13]
sortedArr = mergeSort(unsortedArr)
print("Sorted array:", sortedArr)