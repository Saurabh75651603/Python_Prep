'''
Renamed the function from search to linear_search.

Fixed the comparison in the while loop to check if lst[i] is equal to the target n.

Changed the list variable name from list to lst to avoid conflict with the built-in list type.

Indented the i = i + 1 line properly.

Used global pos instead of globals()['pos'] for clarity.

'''

# pos = -1

def linear_search(lst, target):
    global pos
    i = 0
    while i < len(lst):
        if lst[i] == target:
            pos = i
            return True
        i = i + 1
    return False

lst = [5, 8, 4, 6, 9, 2]
n = 5

if linear_search(lst, n):
    print("Found at", pos + 1)
else:
    print("Not Found")
