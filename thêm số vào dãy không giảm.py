A=[]
n=int(input("nhập n:"))
for i in range(n):
    so=int(input("nhập số thứ" + str(i+1)+":"))
    A.append(so)
x=int(input("nhập số:"))
if x>A[0] and x<A[-1]:
 for i in range(len(A)):
    if x>A[i] and x<A[i+1]:
        A.insert(i+1,x)
else:
    for i in range(len(A)):
        if x<A[0]:
            A.insert(0,x)
            break
        else:
            A.insert(len(A),x)
            break
print(A)
          