n = int(input("Nhập vào giá trị tùy thích n = "))
while n > 0:
    print(n)
    n = n // 2  # Chia lấy phần nguyên
    if n < 10:
        break
"""
Tong = 0
for i in range(0, 11):
    if i == 3 or i == 7:
        continue
    Tong += i
print("Tong =", Tong)
"""
