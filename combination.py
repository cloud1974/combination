def permutation(collection, n, selected=[]):
    if len(selected) == n:
        print(selected)
        return
    for i, x in enumerate(collection):
        permutation(collection[:i]+collection[i+1:], n, selected+[x])

def combination(collection, n, selected=[]):
    global result
    if len(selected) == n:
        if not selected in result:
            print(selected)
            result.append(selected)
        return
    for i, x in enumerate(collection):
        combination(collection[i+1:], n, selected+[x])

# collection中不包含相同元素时可以简化
def combination1(collection, n, selected=[]):
    if len(selected) == n:
        print(selected)
        return
    for i, x in enumerate(collection):
        combination1(collection[i+1:], n, selected+[x])

# 递归调用改写为非递归调用（手工栈方式）
def combination2(collection, n):
    stack = [(collection, [])]
    while len(stack) > 0:
        col, selected = stack.pop()
        if len(selected) == n:
            print(selected)
            continue
        for i in range(len(col)):
            stack.append((col[len(col)-i:], selected+[col[-i-1]]))


class Collection(object):
    def __init__(self, data):
        self.data = data
        self.size = len(data)
        self.result = []
        self.count = 0

    def combination(self, n):
        self.result = []
        self._combo(self.data, n)
        self.count = len(self.result)

    def _combo(self, collection, n, selected=[]):
        if len(selected) == n:
            if not selected in self.result:
                print(selected)
                self.result.append(selected)
        for i, x in enumerate(collection):
            self._combo(collection[i+1:], n, selected+[x])
"""
result = []
data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in range(1, len(data)+1):  
    combination(data, i)
i = 0
for items in result:
    s = sum(items)
    if s > 17 and s < 35:
        i += 1
        print("#%3d: " %i, end="")
        print(" + ".join([str(x) for x in items]), end="")
        print(" = %d" %s)
"""

data = [1, 2, 3, 4, 5]
combination2(data, 3)
