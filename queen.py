N = 8
pos = []
count = 0

def is_ok():
    if len(pos) <= 1:
        return True
    for row, col in enumerate(pos[:-1]):
        y, x = len(pos) - 1, pos[-1]
        if col == x or (x-y == col-row) or (x+y == col+row):
            return False
    return True

def print_pos(pos):
    for row in range(N):
        for col in range(N):
            ch = "Q" if pos[row] == col else "."
            print(ch+" ", end="")
        print("")
    
def queen():
    global pos, count
    if len(pos) == N:
        if is_ok():
            print(pos)
            count += 1
        pos.pop()
    else:
        if is_ok():
            for i in range(N):
                pos.append(i)
                queen()
        if len(pos) > 0:
            pos.pop()

queen()
print("count = %d" %count)