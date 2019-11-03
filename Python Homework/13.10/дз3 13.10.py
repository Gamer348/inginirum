a1=int(0)
b1=int(0)
a2=int(0)
b2=int(0)
while a1<=0:
    a1 = int(input())
while b1<=0:
    b1 = int(input())
while a2<=0:
    a2 = int(input())
while b2<=0:
    b2 = int(input())
if abs(a1-a2) == 5 and abs(b1-b2) == 2 or abs(a2-a1) == 2 and abs(b2-b1) == 5:
    print("YESSSS!")
else:
    print("No No")

