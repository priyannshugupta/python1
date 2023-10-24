# Python code for the implementation of Quick Sort    
  
# Defining the Quick Sort Function    
def quick_sort(arr, low, high):  
    if low < high:  
        # Partition the array and get the pivot index  
        pivot_index = partition(arr, low, high)  
  
        # Recursively sort the left and right subarrays  
        quick_sort(arr, low, pivot_index - 1)  
        quick_sort(arr, pivot_index + 1, high)  
  
# Defining the Partition Function  
def partition(arr, low, high):  
    # Choose the rightmost element as the pivot  
    pivot = arr[high]  
  
    # Initialize the pivot index as the lowest index  
    pivot_index = low  
  
    for i in range(low, high):  
        if arr[i] <= pivot:  
            # Swap the current element with the element at the pivot index  
            arr[i], arr[pivot_index] = arr[pivot_index], arr[i]  
            pivot_index += 1  
  
    # Swap the pivot element with the element at the pivot index  
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]  
  
    return pivot_index  
  
              
# An Array    
array = [23, 42, 3, 83, 36, 49, 19]  
print("The unsorted array is:", array)  
  
# Calling the function  
quick_sort(array, 0, len(array)-1)  
print(f'The sorted array is: {array}')  
