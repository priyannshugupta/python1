# Python code for implementing the Merge Sort  
# Defining merge_sort function  
def merge_sort(arr):  
    # Base case: if the array length is 1 or less,  
    # it is already sorted  
    if len(arr) <= 1:  
        return arr  
  
    # Divide the array into two halves  
    mid = len(arr) // 2  
    left_half = arr[:mid]  
    right_half = arr[mid:]  
  
    # Recursively sort the left and right halves  
    merge_sort(left_half)  
    merge_sort(right_half)  
  
    # Merge the sorted halves by updating the original array  
    merge(arr, left_half, right_half)  
  
# Defining merge Function  
def merge(arr, left, right):  
    i = j = k = 0  
  
    # Compare elements from both lists and  
    # update the original array with the merged elements  
    while i < len(left) and j < len(right):  
        if left[i] < right[j]:  
            # If the element in the left list is smaller,  
            # update the original array with it  
            arr[k] = left[i]  
            i += 1  
        else:  
            # If the element in the right list is smaller,  
            # update the original array with it  
            arr[k] = right[j]  
            j += 1  
  
        k += 1  
  
    # Append any remaining elements  
    # from the left list to the original array  
    while i < len(left):  
        arr[k] = left[i]  
        i += 1  
        k += 1  
  
    # Append any remaining elements  
    # from the right list to the original array  
    while j < len(right):  
        arr[k] = right[j]  
        j += 1  
        k += 1  
  
array = [23, 42, 3, 83, 36, 49, 19]    
print("The given array is:", array)    
    
# Calling the sorting function    
merge_sort(array)    
print("The sorted array is:", array)  
