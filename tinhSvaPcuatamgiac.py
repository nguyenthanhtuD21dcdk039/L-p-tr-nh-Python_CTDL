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


import math

print("Vui lòng nhập vào tọa độ các điểm tương ứng A, B, C")
xA = float(input("Nhập vào tọa độ xA = "))
yA = float(input("Nhập vào tọa độ yA = "))
xB = float(input("Nhập vào tọa độ xB = "))
yB = float(input("Nhập vào tọa độ yB = "))
xC = float(input("Nhập vào tọa độ xC = "))
yC = float(input("Nhập vào tọa độ yC = "))

print("Độ dài 3 cạnh tương ứng là:")
ab = math.sqrt((yB - yA) ** 2 + (xB - xA) ** 2)
bc = math.sqrt((xC - xB) ** 2 + (yC - yB) ** 2)
ca = math.sqrt((xA - xC) ** 2 + (yA - yC) ** 2)

if (ab + bc > ca) and (bc + ca > ab) and (ca + ab > bc):
    print("Ba điểm A,B,C là một tam giác")
    chuvi = ab + bc + ca
    print("Chu vi tam giác ABC = ", chuvi)
    p = chuvi / 2
    Dientich = math.sqrt(p * (p - ab) * (p - bc) * (p - ca))
    print("Diện tích tam giác ABC = ", Dientich)
else:
    print("Ba điểm A,B,C không phải là tam giác")
