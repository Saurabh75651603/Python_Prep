def bubble_sort_with_recursion(arr, n=None):
    
    if n is None:
        n = len(arr)
        
    if n == 1:
        return
    
    for i in range(n-1):
        if arr[i] > arr[i+1]:
            arr[i] , arr[i+1] =  arr[i+1] ,arr[i]
        
    
    bubble_sort_with_recursion(arr, n-1)
    
my_list = [12,24,53,13,75,35,46,243]
bubble_sort_with_recursion(my_list)
print("Sorted Array:" ,my_list)
    
