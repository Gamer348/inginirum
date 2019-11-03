a = int(0)
b=int(0)
c=int(0)
while a<=0:
    a = int( input() )
    break
while b<=0:
    b = int( input() )
    break
while c<=0:
    c = int( input() )
    break
if a ** 2 + b ** 2 == c ** 2 or b ** 2 + c ** 2 == a **2 or a**2 + c**2 == b**2:
    print("YES")
else:
    print("NO")
