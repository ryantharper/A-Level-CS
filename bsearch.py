import sys, math
def bSearch(a,t):
    l=0
    r=len(a)-1
    while True:
        if l>r:
            print("Unsuccessful")
            sys.exit()
        m = math.floor((l+r)/2)
        if a[m]<t:
            l=m+1
        elif a[m]>t:
            r=m-1
        elif a[m]==t:
            print("Done, index:", m)
            sys.exit()


