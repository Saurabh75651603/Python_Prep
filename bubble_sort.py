def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        # Last i elements are already in place, so we don't need to check them
        for j in range(0, n-i-1):
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Example usage
my_list = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(my_list)

print("Sorted array:", my_list)

def bubble_sort_optimized(arr):
    n = len(arr)
    swapped = True

    while swapped:
        swapped = False
        for i in range(1, n):
            if arr[i-1] > arr[i]:
                arr[i-1], arr[i] = arr[i], arr[i-1]
                swapped = True

# Example usage
my_list = [64, 34, 25, 12, 22, 11, 90]
bubble_sort_optimized(my_list)
print("Sorted array:", my_list)

def bidirectional_bubble_sort(arr):
    n = len(arr)
    swapped = True

    while swapped:
        swapped = False

        for i in range(1, n):
            if arr[i-1] > arr[i]:
                arr[i-1], arr[i] = arr[i], arr[i-1]
                swapped = True

        if not swapped:
            break

        swapped = False

        for i in range(n-1, 0, -1):
            if arr[i-1] > arr[i]:
                arr[i-1], arr[i] = arr[i], arr[i-1]
                swapped = True

# Example usage
my_list = [64, 34, 25, 12, 22, 11, 90]
bidirectional_bubble_sort(my_list)
print("Sorted array:", my_list)

def recursive_bubble_sort(arr, n=None):
    if n is None:
        n = len(arr)

    if n == 1:
        return

    for i in range(n-1):
        if arr[i] > arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]

    recursive_bubble_sort(arr, n-1)

# Example usage
my_list = [64, 34, 25, 12, 22, 11, 90]
recursive_bubble_sort(my_list)
print("Sorted array:", my_list)

def bubble_sort_early_exit(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True

        if not swapped:
            break

# Example usage
my_list = [64, 34, 25, 12, 22, 11, 90]
bubble_sort_early_exit(my_list)
print("Sorted array:", my_list)

