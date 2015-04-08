#demonstrates use of cloning for lists
#now I am adding some commented text
def removeDupsBetter(L1, L2):
    L1Start = L1[:]#makes a copy
    for e1 in L1Start:#iterates over a copy
        if e1 in L2:
            L1.remove(e1)

L1 = [1,2,3,4]
L2 = [1,2,5,6]
removeDupsBetter(L1, L2)
print(L1)