import re
addressAbrv = {"Street": "St.",
               "Road": "Rd.",
               "Drive": "Dr.",
               "Avenue": "Ave.",
               "Terrace": "Ter.",
               "Lane": "Ln."}

file = open("DummyAddresses2.txt", "r")
newFile = open("NewAddresses.txt", "w")

addrs = []

#addrs = [line.replace(address,addressAbrv[address]) for line in file for address in line.split() if address in addressAbrv]

for line in file:
    for i,p in enumerate(line.split()):
        if i == len(line.split())-1:
            print(p)

#re.sub(r'Street\Z', 'St.', '23 Streetly Street')  

"""
for line in file:
    for address in line.split():
        if address in addressAbrv:
            addrs.append(line.replace(address,addressAbrv[address]))

for address in addrs:
    newFile.write(address.upper())
"""
newFile.close()
file.close()
    
