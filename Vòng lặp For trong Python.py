# Vòng lặp For đi từ 0 đến bé hơn n, mỗi lần tăng lên 1 đơn vị
# For example: Tính tổng từ 0 - n
n = int(input("Nhập vào giá trị n = "))
tong = 0
for i in range(n + 1):
    tong += i
print("tong = ", tong)

# Vòng lặp for có bước tăng tùy chỉnh
for i in range(0, 10, 2):  # Bắt đầu từ 0 đến <10. Và mỗi lên tăng lên 2 đơn vị
    print(i)

for i in range(10, 0, -1):  # Bắt đầu từ 10 về >0. Và mỗi lần giảm 1 đơn vị
    print(i)

# Vòng lặp for duyệt các phần tử của list
colors = ["Thanh Tú", "Hoa Hiền"]
for color in colors:  # color sẽ được gán bằng từng phần tử và đc in ra ngoài màn hình
    print(color)

# Vòng lặp for duyệt phần tử theo vị trí
for i in range(len(colors)):
    print(colors[i])
