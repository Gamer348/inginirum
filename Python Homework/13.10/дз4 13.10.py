a1=int(0)
b1=int(0)
a2=int(0)
b2=int(0)
a3=int(0)
b3=int(0)
a4=int(0)
b4=int(0)
a5=int(0)
b5=int(0)
a6=int(0)
b6=int(0)
a7=int(0)
b7=int(0)
a8=int(0)
b8=int(0)
while a1==0 or a1>8:
 a1 = int(input())
while b1==0 or b1>8:
 b1 = int(input())
while a2==0 or a2>8:
 a2 = int(input())
while b2==0 or b2>8:
 b2 = int(input())
while a3==0 or a3>8:
 a3 = int(input())
while b3==0 or b3>8:
 b3 = int(input())
while a4==0 or a4>8:
 a4 = int(input())
while b4==0 or b4>8:
 b4 = int(input())
while a5==0 or a5>8:
 a5 = int(input())
while b5==0 or b5>8:
 b5 = int(input())
while a6==0 or a6>8:
 a6 = int(input())
while b6==0 or b6>8:
 b6 = int(input())
while a7==0 or a7>8:
 a7 = int(input())
while b7==0 or b7>8:
 b7 = int(input())
while a8==0 or a8>8:
 a8 = int(input())
while b8==0 or b8>8:
 b8 = int(input())
if a1==a2 or a1==a3 or a1==a4 or a1==a5 or a1==a6 or a1==a7 or a1==a8:
    print("YES")
elif a2==a1 or a2==a3 or a2==a4 or a2==a5 or a2==a6 or a2==a7 or a2==a8:
    print("YES")
elif a3==a1 or a3==a2 or a3==a4 or a3==a5 or a3==a6 or a3==a7 or a3==a8:
    print("YES")
elif a4==a1 or a4==a2 or a4==a3 or a4==a5 or a4==a6 or a4==a7 or a4==a8:
    print("YES")
elif a5==a1 or a5==a2 or a5==a4 or a2==a5 or a2==a6 or a2==a7 or a2==a8:
    print("YES")
elif a6==a1 or a6==a2 or a6==a3 or a6==a4 or a6==a5 or a6==a7 or a6==a8:
    print("YES")
elif a7==a1 or a7==a2 or a7==a3 or a7==a4 or a7==a5 or a7==a6 or a7==a8:
    print("YES")
elif a8==a1 or a8==a2 or a8==a3 or a8==a4 or a8==a5 or a8==a6 or a8==a7:
    print("YES")
elif b1==b2 or b1==b3 or b1==b4 or b1==b5 or b1==b6 or b1==b7 or b1==b8:
    print("YES")
elif b2==b1 or b2==b3 or b2==b4 or b2==b5 or b2==b6 or b2==b7 or b2==b8:
    print("YES")
elif b3==b1 or b3==b2 or b3==b4 or b3==b5 or b3==b6 or b3==b7 or b3==b8:
    print("YES")
elif b4==b1 or b4==b2 or b4==b3 or b4==b5 or b4==b6 or b4==b7 or b4==b8:
    print("YES")
elif b5==b1 or b5==b2 or b5==b4 or b5==b4 or b5==b6 or b5==b7 or b5==b8:
    print("YES")
elif b6==b1 or b6==b2 or b6==b3 or b6==b4 or b6==b5 or b6==b7 or b6==b8:
    print("YES")
elif b7==b1 or b7==b2 or b7==b3 or b7==b4 or b7==b5 or b7==b6 or b7==b8:
    print("YES")
elif b8==b1 or b8==b2 or b8==b3 or b8==b4 or b8==b5 or b8==b6 or b8==b7:
    print("YES")
else:
    print("NO")