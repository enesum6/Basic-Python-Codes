def remove_dups(L1,L2):
    L1_copy=L1[:]
    for e in L1:
        if e in L2:
            L1.remove(e)
    
L1=[10,20,30,40]
L2=[10,20,50,60]
remove_dups( L1,L2)
print(L1)