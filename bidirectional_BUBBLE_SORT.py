'''
Bidirectional Bubble Sort, also known as Cocktail Shaker Sort or Shaker Sort, 
is a variation of the Bubble Sort algorithm. It works by iteratively moving through 
0the array in both directions, alternatively from left to right and from right to left, 
comparing and swapping adjacent elements if they are in the wrong order. 
This bidirectional movement can lead to faster convergence of smaller elements to one end
and larger elements to the other.
'''

def bidirectional_bubble_sort(arr):
    
    n = len(arr)
    swapped = True
    
    while swapped:
        swapped = False
        
        
        for i in range(1,n):
            if arr[i-1] > arr[i]:
                   arr[i-1] , arr[i] = arr[i], arr[i-1]
                   swapped = True

                                    
        if not swapped:
            break
        
        
        swapped = False
        
        for i in range(1,n):
            if arr[i-1] > arr[i]:
                   arr[i-1] , arr[i] = arr[i], arr[i-1]
                   swapped = True

                    
                    
my_list = [33,34,46,57,68,34,56,34,67,35,24,13,1361,16,25,124,35]
print(my_list)

bidirectional_bubble_sort(my_list)
print("Sorted Array :", my_list)
                                