#giải phương trình bậc hai
a=float(input("nhập hệ số a:"))
b=float(input("nhập hệ số b:"))
c=float(input("nhập hệ số c:"))
d=b**2-4*a*c
print("delta=",d)
if d<0:
    print("phương trình vô nghiệm")
if d==0:
    print("phương trình có nghiệm kép")
    x=-b/(2*a)
    print("phương trình có nghiệm duy nhất x=",x)
import math
if d>0:
    print("phương trình có hai nghiệm phân biệt")
    x1=(-b+ math.sqrt(d))/(2*a)
    x2=(-b- math.sqrt(d))/(2*a)
    print("phương trình có nghiệm x1, x2 là:",x1,x2)
    
    
    

    

      


