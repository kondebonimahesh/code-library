ar = [2,0,8,5,4,3,2,1]
n=len(ar)
#bym
for i in range(1,n) :
    for j in range(i,0,-1) :
        if ar[j]<ar[j-1] :
            ar[j],ar[j-1]=ar[j-1],ar[j]
        else :
            break 
    
print(ar)

