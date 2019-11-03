a_string = "*"
b_string = "+"
c_string = "-"
d_string = "/"
A = float(input())
B = float(input())
C = input()
if C == a_string:
    print(A*B)
elif C == b_string:
    print(A+B)
elif C == c_string:
    print(A-B)
elif C == d_string:
    print(A/B)
elif B == 0 and C == d_string:
    print("ЫЫЫЫЫЫ")
else:
    print("ЫЫЫЫЫЫ")