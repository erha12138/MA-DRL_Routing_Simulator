# a generator that yields items instead of returning a list
def firstn(n):
    num = 0
    while num < n:
        yield num
        num += 1

x = firstn(1000000)

for i in range(100):
    print(next(x))

sum_of_first_n = sum(firstn(1000000))
print(firstn(1000000))
print(sum_of_first_n)