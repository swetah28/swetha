a=123
sum=0
while a>0:
    n=a%10
    sum=sum*10+n
    a=a//n
print(sum)
