#2 int input and console x as lower limit and y as upper limit. wap to find prime no.s btw x and y

a=int(input())
b=int(input())
c=0
if(a<b):
    x=a
    y=b
else:
    x=b
    y=a
for i in range(x+1,y):
    for j in range(1,i):
        if(i%j==0):
            c+=1
    if(c==1):
        print(i)
    c=0
    
