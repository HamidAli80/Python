name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
names = dict()
for line in handle: 
    if not line.startswith('From'):
        continue
    else:
        address = line.split()
        if len(address) > 3:
            name = address[1]
            names[name] = names.get(name, 0)  +1
maxValue = None

for k, v in names.items():
    if maxValue is None or maxValue < v :
        nam = k
        maxValue = v
print(nam, maxValue)
    
