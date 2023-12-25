def early_exit_bubble_sort(arr): # takes 'arr' as an argument
    
    n = len(arr) # assigns the length of arr to var n
    for i in range(n): # Initiates an outer loop that iterates n times, representing the number of elements in the array.
        swapped = False # declares the boolean to swapped as false
        for j in range(0,n-i-1): # Initiates an inner loop that iterates through the unsorted part of the array. The range 0 to n-i-1 ensures that the loop doesn't include elements that have already been sorted in previous iterations.
            if arr[j] > arr[j+1]: # Checks if the current element is greater than the next element. If true, it means the elements are in the wrong order.
                arr[j], arr[j+1] = arr[j+1], arr[j] # Swaps the current element and next element 
                swapped = True # to indicate that a swap occurred during this pass
                
        if not swapped: # if no swaps occurred during the inner loop
            break

my_list = [31,35,4,69,6,25,14,35,47,24]
early_exit_bubble_sort(my_list)
print("Sorted Array:" ,my_list)

                
                
    