arr =[4,5,6,1,2]
#by me
n=len(arr)
for i in range(n) :
    for j in range(n-i) :
        if j>0 and arr[j]<=arr[j-1] :
            arr[j],arr[j-1]=arr[j-1],arr[j]
    
print(*arr)
