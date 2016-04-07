name = [[],[],[]]
with open('test.txt') as f:
    for line in f:
        for each in enumerate(line.split()):
            name[each[0]].append(float(each[1]))
a,b,c = name

