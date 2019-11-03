A = int( input() )
B = int( input() )
if A == 0 or B == 0:
    NOD = 0
while A > 0 and B > 0:
    if A>B:
        A %= B
    else: 
        B %= A
    NOD = A + B
print("NOD:",NOD,sep="")