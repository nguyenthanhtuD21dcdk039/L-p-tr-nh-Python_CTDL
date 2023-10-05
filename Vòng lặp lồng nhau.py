for j in range(2, 10):
    print("Bảng cửu chương", j)  # Bảng cửu chương bắt đầu từ 2 - 9
    for i in range(1, 11):  # i sẽ chạy trong khoảng 1-10
        print("{0} * {1} = {2}".format(j, i, j * i))
