
def my_generator():
    n = 1
    print("apples")
    yield n           # returns the value and remembers the yield                       that was called
    n += 9
    print("Oranges")
    yield n
    n += 10
    print("Pine")
    yield n

res = my_generator()
print(res)

print(res.__next__())
print(res.__next__())
print(res.__next__())

# print(res.__next__())

def get_val():
   for i in range(1, 11):
       yield i

res = get_val()
print(next(res))
print(next(res))
print(next(res))
print(next(res))
print(next(res))
print(next(res))
print(next(res))
print(next(res))
print(next(res))
print(next(res))

