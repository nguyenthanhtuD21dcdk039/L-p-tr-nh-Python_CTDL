# Sự khác nhau giữa vòng lặp for và while
# Vòng lặp For được dùng khi chúng ta xác định được số lần lặp đi lặp lại.
# Và vòng For hầu hết là xác định đc số lần lặp
# Còn đối với vòng lặp while được dùng khi chúng ta ko biết trc đc số lần lặp
n = -1
while n <= 0:
    n = int(input("Nhập vào giá trị của n = "))
i = 0
tong = 0
while i <= n:
    tong += i  # Tổng = Tổng + i
    i += 1  # i = i + 1
print("Tổng = ", tong)

# Vòng lặp while có thể kết hợp với từ khóa else. Trong trường hợp vòng lặp While sai thì vẫn đc
# in ra biến của else.

j = 0
n = int(input("Nhập vào giá trị của n tùy thích = "))
while j <= n:
    print(j, " -Bên trong vòng lặp")
    j += 1
    if j >= 5:  # Nếu trong trường hợp j>=5 thì câu lệnh break sẽ dc thực hiện.
        # Và câu lệnh else sẽ ko đc in ra màn hình. Và ngược lại.
        break
else:
    print("- Bên ngoài vòng lặp")
