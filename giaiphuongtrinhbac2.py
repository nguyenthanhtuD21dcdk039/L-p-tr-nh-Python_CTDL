import math

print("Giải phương trình bậc 2 có dạng ax^2+bx+c=0 ")
a = float(input("Nhập vào giá trị của a = "))
b = float(input("Nhập vào giá trị của b = "))
c = float(input("Nhập vào giá trị của c = "))
print("Phương trình bậc 2: {0}x^2+{1}x+{2}=0".format(a, b, c))

if a != 0:
    delta = b**2 - 4 * a * c
    if delta < 0:
        print("Phương trình vô nghiệm")
    elif delta == 0:
        x = -b / (2 * a)
        print("Phương trình có nghiệm kép x1=x2=", x)
    else:
        x1 = (-b - math.sqrt(delta)) / (2 * a)
        x2 = (-b + math.sqrt(delta)) / (2 * a)
        print("Phương trình có 2 nghiệm phân biệt x1={0} và x2={1}".format(x1, x2))
else:
    print("Không thỏa điều kiện Phương trình bậc 2")
