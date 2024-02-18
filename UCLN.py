n=input("nhập 2 số tự nhiên:")
k=n.split( )
a=int(k[0])
b=int(k[1])
r=a%b
while r!=0:
    a=b
    b=r
    r=a%b
print(b)