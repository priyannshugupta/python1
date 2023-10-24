# Python code to show how to implement the selection sort    
    
# Defining the function    
def selection_sort(array):    
    # Looping through every element of the array except the last  
    for i in range(len(array)-1):    
    
        # Searching the minimum element in subarry[i+1 to last element]   
        min_index = i    
        for j in range(i + 1, len(array)):    
            if array[min_index] > array[j]:    
                min_index = j    
    
        # Swaping the minimum element and the first element       
        array[i], array[min_index] = array[min_index], array[i]    
    
# An array    
array = [23, 42, 3, 83, 36, 49, 19]  
    
# Calling the function  
selection_sort(array)    
    
print("The sorted array is:", array)  
