arr = [1,2,43,32,5,4,62]

print("Choose any one of the given numbers you want to search for: \n", arr)
Num = int(input("Enter the number you want to search:"))

Found = False

for i, element in enumerate(arr):
    if Num == element:
        Found = True
        break
    
if Found:
    print(f"The element found at index number" ,{i + 1})
else:
    print(f"The element you want to search was not found")















































# for element in arr:
#     if Num == arr:
#        Found = True
#        break
   
   
# if Found:
#      print("The number found at index number: ",{i})
# else:
#      print("The number not found")











# if Num == arr:
#     print ("Found!")
# else:
#     print("Not found")