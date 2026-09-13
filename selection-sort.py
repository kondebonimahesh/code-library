arr =[4,5,6,1,2]
# byme
n=len(arr)
for i in range(n) :
    k=i
    for j in range(i+1,n) :
        if arr[j]<arr[k] :
            k=j 
    arr[k],arr[i]=arr[i],arr[k]

print(*arr)
