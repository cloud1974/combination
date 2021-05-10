def search(func, x, low, high):
    while high - low > 1e-10:
        mid = (high + low) / 2
        if func(mid) > x:
            high = mid
        else:
            low = mid
    return low

def square(x):
    return x * x

def lstTrue(func, low, high):
    while low <= high:
        mid = (low + high) // 2
        if func(mid):
            low = mid + 1
        else:
            high = mid - 1
    return low - 1

def lstTrue1(func, low, high):
    step = (high - low) // 2
    while step >= 1:
        while func(low+step):
            low += step
        step //= 2
    return low

def func1(x):
    return True

def search1():
    pos, max = 0, int(2e9)
    a = max
    while a >= 1:
        if check(pos+a):
            pos += a
        a //= 2
    return pos

def check(x):
    return x == 10

print(search1())
#print(lstTrue1(func1, 2, 10))
#print("%.9f" %search(square, 100, 0, 10)) 