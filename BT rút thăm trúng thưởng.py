# Khai báo thư viện Ramdom
import random

# Khai báo set
thungPhieu = set()

# if x in thungPhieu: KT xem số điện thoại này đã nằm bên trong thùng phiếu hay chưa
# Vòng lặp
while True:
    print("-----*****MENU*****-----")
    print("Vui lòng lựa chọn chức năng: ")
    print("1- Thêm một số điện thoại vào thùng phiếu dự thưởng")
    print("2- Xóa một số điện thoại từ thùng phiếu dự thưởng")
    print("3- Quay số ngẫu nhiên lấy ra một số điện thoại trúng thưởng")
    print("Thùng phiếu hiện tại: ")
    print(thungPhieu)

    luachon = int(input("Lựa chọn: "))

    if luachon == 1:
        SoDienThoai = input("Nhập vào số điện thoại dự thưởng: ")
        thungPhieu.add(SoDienThoai)
    elif luachon == 2:
        SoDienThoai = input("Nhập vào số điện thoại dự thưởng cần xóa:")
        thungPhieu.discard(SoDienThoai)
    elif luachon == 3:
        index = random.randint(
            0, len(thungPhieu) - 1
        )  # Chỉ lấy ra được 1 số điện thoại trúng thưởng duy nhất
        print("Vị trí trúng thưởng" + str(index))

        tmp = thungPhieu.copy()
        i = 0
        for x in tmp:
            if i == index:
                break
            i = i + 1
            print("Chúc mừng Số Điện Thoại: " + x + " đã may mắn trúng thưởng !")
            thungPhieu.discard(x)
            del tmp
        else:
            break

    x = input("Nhập phím bất kỳ để tiếp tục chương trình: ")
