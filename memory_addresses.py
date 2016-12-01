zeroToF = [hex(x)[2:] for x in range(256)]
memAdrs = {k:"" for k in zeroToF}

# finds a free space, loops thru list so added/multiplied val isn't placed
# in random mem address - placed in next empty location
def freeSpace():
    for k in zeroToF:
        if memAdrs[k] == "":
            return k

def read():
    memLoc = str(input("What address?: ")).lower()
    print(memAdrs[memLoc])

def write():
    memLoc = str(input("What address?: ")).lower()
    data = input("Enter data: ")
    memAdrs[memLoc] = data

def add():
    try:
        memLoc1 = str(input("What address?: ")).lower()
        memLoc2 = str(input("What address?: ")).lower()
        added = int(memAdrs[memLoc1]) + int(memAdrs[memLoc2])
        free = freeSpace()
        memAdrs[free] = str(added)
        print(str(added) + " stored in memory location " + str(free))
    except:
        yn = str(input("A memory address is either empty or not an integer. Would you like to go back to the main program? yes/no "))
        if yn == 'yes':
            main()
        else:
            add()

def main():
    operation = str(input("Operation? Read, Write, Add, Multiply: ")).lower()
    print("MEMORY ADDRESSES: ", zeroToF)
    if operation.startswith('r'):
        read()
    elif operation.startswith('w'):
        write()
    elif operation.startswith('a'):
        add()
    main()
main()
