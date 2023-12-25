def my_generator():
    yield 1
    yield 2 
    yield 3
    yield 4
    
gen = my_generator()

# print(gen)

# for i in gen:
#     print(i)
    

print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
