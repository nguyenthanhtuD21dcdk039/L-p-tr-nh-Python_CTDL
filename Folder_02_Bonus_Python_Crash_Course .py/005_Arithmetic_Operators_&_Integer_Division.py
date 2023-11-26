"""
print("Mời Thanh Tú nhập vào giá trị của a")
a = int(input("a = "))
print("Mời Thanh Tú nhập vào giá trị của b")
b = int(input("b = "))

print("{0}+{1}={2}".format(a, b, a + b))
print("{0}-{1}={2}".format(a, b, a - b))
print("{0}*{1}={2}".format(a, b, a * b))
print("{0}/{1}={2}".format(a, b, a / b))
print("{0}%{1}={2}".format(a, b, a % b)) # Trả về phần dư của phép chia
print("{0}**{1}={2}".format(a, b, a**b))
print("{0}//{1}={2}".format(a, b, a // b)) # Lấy kết quả là phần nguyên
"""
import math  # Khai báo thư viện để có thể sử dụng các hàm trong math

x = float(input("Nhập vào giá trị của x = "))
y = float(input("Nhập vào giá trị của y = "))
z = float(input("Nhập vào giá trị của z = "))
print("|x| = ", math.fabs(x))  # Lấy trị tuyệt đối
print("sqrt(x) = ", math.sqrt(x))  # Lấy căn bậc 2
print("ceil(x) = ", math.ceil(y))  # Làm tròn lên giá trị phía trên vd: 4.3=5
print("floor(x) = ", math.floor(z))  # Làm tròn xuống giá trị phía dưới vd: 4.8=4
