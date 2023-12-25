num = [1, 2, 4, 4]

it = iter(num)

print(it.__next__())
print(it.__next__())
print(it.__next__())
print(it.__next__())

# print(next(it))
try:
    print(next(it))
except StopIteration:
    print("End of iteration")
