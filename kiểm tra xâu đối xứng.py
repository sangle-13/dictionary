#kiểm tra xâu đối xứng
n=input("nhập xâu:")
k= True
for i in range(len(n)):
    if n[i]!=n[-(i+1)]:
        k= False
if k==True:
    print("yes")
else:
    print("no")