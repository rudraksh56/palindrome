a=int(input('enter the no by user'))
n=0
m=a
while(a>0):
    c=a%10
    n=10*n+c
    a=a//10
print(n)
if(m==n):
    print(m ,'is a palindrome')
else:
    print(m,' is not palindrome')
