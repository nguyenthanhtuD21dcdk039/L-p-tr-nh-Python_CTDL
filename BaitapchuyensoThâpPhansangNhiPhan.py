# Bài tập chuyển đổi từ thập phân sang Nhị Phân
# Nhập n (n>0)
n = -1
while n <= 0:
    n = int(input("Nhập vào giá trị của n (n>0) = "))
# CHuyển từ thập phân sang nhị phân
x = n
KetQua = ""
while n > 0:
    KetQua = str(n % 2) + KetQua
    print("n%2 = ", n % 2)  # % là phép chia lấy dư
    n = n // 2  # // Phép chia lấy phần nguyên
    print("n = ", n)
print("Kết quả = ", KetQua)
