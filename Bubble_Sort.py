# Python code to implement the bubble sort  
  
# Defining the function  
def bubble_sort(array):  
    length = len(array)  
  
    # Looping through every element of the given array except the last  
    for i in range(length - 1):  
  
        # Last i elements of the array are sorted first  
        for k in range(0, length - i - 1):  
  
            # looping through the array from 0 to length-i-1  
            # Swapping the elements which are in unsorted order  
            if array[k] > array[k + 1]:  
                array[k], array[k + 1] = array[k + 1], array[k]  
  
# An array  
array = [23, 42, 3, 83, 36, 49, 19]  
  
# Calling the function  
bubble_sort(array)  
  
print("The sorted array is:", array)  
