"""
n = -1
while n <= 0:
    n = int(input("Nhập vào giá trị của n = "))
i = 0
tong = 0
while i <= n:
    tong += i  # Tổng = Tổng + i
    i += 1  # i = i + 1
print("Tổng = ", tong)
"""
n = int(input("Nhập vào giá trị n = "))
tong = 0
for i in range(n + 1):
    tong += i
print("tong = ", tong)
