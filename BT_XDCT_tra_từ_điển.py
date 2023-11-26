# Khai báo
tuDien = {}

while True:
    print("Vui lòng lựa chọn chức năng của chương trình: ")
    print(
        """
        1. Thêm một từ vựng mới và ý nghĩa của từ vựng vào từ điển: \n
        2. Tra cứu ý nghĩa của một từ vựng: \n
        3. Cập nhật một ý nghĩa mới cho từ vựng: \n
        4. Cho phép người dùng xóa đi một từ vựng trong từ điển: \n
        5. Cho phép người dùng xóa toàn bộ từ vựng: \n
        6. Cho phép người dùng in ra toàn bộ từ vựng: \n
        7. Cho phép người dùng in ra toàn bọ từ điển theo cấu trúc: "Từ Vựng" : "Ý Nghĩa" \n
        8. Kết thúc chương trình! \n
"""
    )

    luaChon = int(input("Nhập vào lựa chọn của bạn: "))

    if luaChon == 1:
        tuVung = input("Nhập vào một từ vựng: ")
        yNghia = input("Nhập vào ý nghĩa của từ vựng: ")
        tuDien[tuVung] = yNghia
        print("Đã cập nhật dữ liệu thành công")
    elif luaChon == 2:
        tuVung = input("Nhập vào từ vựng cần tra nghĩa: ")
        print("Ý nghĩa: ", tuDien[tuVung])
    elif luaChon == 3:
        tuVung = input("Nhập vào một từ vựng mới cần cập nhật: ")
        yNghia = input("Ý nghĩa của từ vựng mới: ")
        tuDien[tuVung] = yNghia
    elif luaChon == 4:
        tuVung = input("Nhập vào từ vựng cần xóa: ")
        tuDien.pop(tuVung)
        print("Đã xóa từ vựng thành công!")
    elif luaChon == 5:
        tuDien.clear()
        print("Đã xóa toàn bộ từ vựng có trong từ điển thành công!")

    elif luaChon == 6:
        print("Danh sách từ vựng có trong từ điển: ")
        for x in tuDien.keys():
            print(x)

    elif luaChon == 7:
        print("Danh sách các từ vựng có trong từ điển: ")
        for x, y in tuDien.items():
            print(x, ":", y)

    elif luaChon == 8:
        break

    else:
        print("Bạn đã nhập lựa chon không chính xác")
