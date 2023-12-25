# Binary Search Algorithm using Iterative Function

# pos = -1       # Declaring a global variable outside the func()


def binary_search(arr_item, search_item): # Declaring a func() with 2 parameters
    
    global pos                         # Declaring a global variable inside the func()
    lower_bound = 0                    # Defining lower_bound with 0
    upper_bound = len(arr_item) - 1    # Defining upper_bound with length of given array to -1
    
    while lower_bound <= upper_bound:  # Comparing the lower and upper bound using while loop
        mid_item = (lower_bound + upper_bound) // 2   # Defining the mid_item by integer dividing the lower and upper bound
        
        if arr_item[mid_item] == search_item:   # Using if conditional, is the value that is to be search and any of the value of given arr_item is same?
            pos = mid_item                      # Updating the value of local variable by mid_item
            return True                         
        else:
            if arr_item[mid_item] < search_item: # Nesting the if statement in else block for checking the following condition and updating the values.
                lower_bound =  mid_item +1
            else:
                upper_bound = mid_item -1
    return False

arr_item = [12,23,34,45,56,67,78,89,90]
search_item = 89

if binary_search(arr_item, search_item):
    print(f"The element you was searching found at index number",pos +1)
else:
    print(f"{search_item} not found") 