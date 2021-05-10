with open("data.txt", encoding="utf-8") as fin:
    clean_data = fin.readline().strip().replace(" ", "").replace("，", ",")
    data = eval("[" + clean_data + "]")
print('Read %d numbers from file "data.txt".' %len(data))
print("Sort and count result:")
with open("sorted_data.txt", "w", encoding="utf-8") as fout:
    for x in sorted(list(set(data))):
        print("%d: %d" %(x, data.count(x)))
        fout.write("%d: %d\n" %(x, data.count(x)))
print('Result data stored in file "sorted_data.txt".')
