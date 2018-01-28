a_x = int(input())
a_y = int(input())
b_x = int(input())
b_y = int(input())
c_x = int(input())
c_y = int(input())
AB2 = (a_x - b_x) ** 2 + (a_y - b_y) ** 2
AC2 = (a_x - c_x) ** 2 + (a_y - c_y) ** 2
BC2 = (c_x - b_x) ** 2 + (c_y - b_y) ** 2
if  BC2 == AB2 + AC2 or AC2 == AB2 + BC2 or AB2 == AC2 + BC2:
    print("yes")
else:
    print("no")
