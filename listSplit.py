# romeo.txt
fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    splitline = line.split()
    for x in splitline:
        if x in lst:
            continue
        lst.append(x)

lst.sort()        
print(lst)