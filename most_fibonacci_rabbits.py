
with open('rosalind_fibd (1).txt') as f:
    x,y=f.readline().strip().split()
print(x,y)

dict={}
def fib(n,k):
    dict[0],dict[1]=1,1
    for i in range(2,n):
            if i>k:
                dict[i]=dict[i-1]+dict[i-2]-dict[i-(k+1)]
            elif i==k or i==(k+1):
                dict[i] = dict[i - 1] + dict[i - 2]-1

            else:
                dict[i] = dict[i - 1] + dict[i - 2]
    return dict[n-1]
print(fib(int(x),int(y)))