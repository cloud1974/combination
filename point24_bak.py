solutions = set()

def point24(expression, numbers):
    global solutions
    if len(numbers) == 0:
        if eval(expression) == 24:
            solutions.add(expression)
    elif expression == "":
        for i, n in enumerate(numbers):
            point24(str(n), numbers[:i]+numbers[i+1:])
    else:
        for op in "+-*/":
            for i, n in enumerate(numbers):
                point24("("+expression+op+str(n)+")", numbers[:i]+numbers[i+1:])
                if op == "-" or (op == "/" and eval(expression) != 0):
                    point24("("+str(n)+op+expression+")", numbers[:i]+numbers[i+1:])

point24("", [3, 7, 9, 13]) # 测试用例。一个1和三个5算24点有解：1除以5等于0.2，5减去0.2等于4.8，4.8乘以5等于24
print("Found %d solutions." %len(solutions))
for i, s in enumerate(solutions):
    print("%d: %s = 24" %(i+1, s))


        