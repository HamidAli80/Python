import re
hand = open('actualFile.txt')
lst = list()
for line in hand:
    line = line.rstrip()
    x = re.findall('([0-9]+)', line)
    if len(x) > 0:
        lst.append(x)
flat_list = [item for sublist in lst for item in sublist]
res = [float(ele) for ele in flat_list]
total = sum(res)
print(total)