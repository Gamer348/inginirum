a = int(input())
a_string = "@"
b_string = "@@"
c_string = ""
d_string = " "
for i in range (1,a):
    print(d_string * (a-i) + a_string + c_string)
    c_string = c_string + b_string
