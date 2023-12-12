# L = [-9,4,5,2,-6,7,5,-5]
def foo(L):
    for i in range(len(L)):
        if len(L) > 1:
            if L[1]<1:
                del(L[1])
            elif L[0]<1:
                del(L[0])
            elif L[0] >L[1]:
                del(L[0])
            else:
                del(L[1])
    return L
print(foo([-9,23,4,1,5,22,-6,7,5,-5,0]))