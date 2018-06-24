
def isLucky(n):
    a=""
    while n != 0:
        a=a+str(n%10)
        n=n//10
    print a

n=123321
print isLucky(n)