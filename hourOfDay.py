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
            name = address[5]
            hour = name.split(':')
            names[hour[0]] = names.get(hour[0], 0)  +1
names = sorted(names.items())
for k, v in names:
    print(k, v)