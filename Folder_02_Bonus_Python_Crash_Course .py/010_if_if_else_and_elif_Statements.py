"""
import math

# Khai báo tọa độ 3 cạnh bất kỳ của một tam giác
xA = float(input("Nhập vào tạo độ xA = "))
yA = float(input("Nhập vào tạo độ yA = "))
xB = float(input("Nhập vào tạo độ xB = "))
yB = float(input("Nhập vào tạo độ yB = "))
xC = float(input("Nhập vào tạo độ xC = "))
yC = float(input("Nhập vào tạo độ yC = "))

# Tính độ dài của 3 cạnh tam giác
ab = math.sqrt((xB - xA) ** 2 + (yB - yA) ** 2)
bc = math.sqrt((xC - xB) ** 2 + (yC - yB) ** 2)
ca = math.sqrt((xA - xC) ** 2 + (yA - yC) ** 2)

# Kiểm tra điều kiện có thỏa là một tam giác hay không?
if (ab + bc > ca) and (bc + ca > ab) and (ca + ab > bc):
    print("Vậy ba cạnh trên đã tạo thành một tam giác")
    cv = ab + bc + ca
    print("Chu vi tam giác ABC = ", cv)
    p = cv / 2
    s = math.sqrt(p * (p - ab) * (p - bc) * (p - ca))
    print("Diện tích tam giác ABC = ", s)
else:
    print("Không thỏa điều kiện là một tam giác")
"""
"""
x = int(input("Nhập vào giá trị của x = "))

if x > 0:
    print(x, "là số dương")
if x % 2 == 0:
    print(x, "cũng là số chẵn")
else:
    print(x, "cũng là số lẽ")
print("Kết thúc chương trình")
"""
import math

x = input("Nhập điểm tổng kết: ")
x = float(x)
if x >= 8.0:
    print(x, "Đủ điều kiện học sinh giỏi")
elif x >= 6.5:
    print(x, "Đủ điều kiện học sinh Khá")
elif x >= 5.0:
    print(x, "Đủ điều kiện học sinh Trung Bình")
else:
    print(x, "Đạt danh hiệu học sinh Kém")
print("Kết thúc chương trình")
