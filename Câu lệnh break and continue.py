# Continue là bỏ qua phần còn lại khi gặp điều kiện đúng và sau đó tiếp tục thực hiện vòng lắp tiếp theo
# break là giúp ngưng luôn vòng lặp khi thỏa mãn 1 điều kiện nào đó

for i in range(0, 10):
    print(i)
    if i > 5:
        break

n = int(input("Nhập vào giá trị tùy thích n = "))
while n > 0:
    print(n)
    n = n // 2  # Chia lấy phần nguyên
    if n < 10:
        break

for i in range(2, 10):
    print("Bảng cửu chương", i)
    for j in range(1, 11):
        print("{0} * {1} = {2}".format(i, j, i * j))
        if j > 4:
            break
