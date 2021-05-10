def combination(collection, n, selected=[]):
    global result
    if len(selected) == n:
        if not selected in result:
            if sum(selected) > 17 and sum(selected) < 35:
                result.append(selected)
        return
    for i, x in enumerate(collection):
        combination(collection[i+1:], n, selected+[x])

result = []
data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in range(1, len(data)+1):  
    combination(data, i)
for i, x in enumerate(result):
    print("#%3d: " %(i+1), end="")
    print(" + ".join([str(d) for d in x]), end="")
    print(" = %d" %sum(x))
print("共找到%d个符合要求的数字组合。" %len(result))