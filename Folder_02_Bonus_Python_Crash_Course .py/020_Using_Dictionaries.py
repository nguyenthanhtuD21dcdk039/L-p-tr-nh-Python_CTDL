"""
Từ điển đc use để lưu trữ các giá trị dữ liệu(data value) trong các cặp key: value.
Từ điển là 1 tập hợp đc sắp xếp theo tứ tự *, có thể thay đổi và ko cho phép trùng lặp.
Từ điển được viết bằng dấu ngoặc nhọn và có các khóa và giá trị
Từ điển có thể thay đổi, nghĩa là chúng ta có thể thay đổi, 
thêm hoặc bớt các mục sau khi dictionary được khởi tạo.
Từ điển ko thể có 2 mục với cùng 1 khóa
"""
"""
sinhvien = {
    "hoVaten": "Nguyễn Thanh Tú",
    "Masosinhvien": "N21DCDK039",
    "Malop": "N21CQDK01-N",
    "Khoa": "Kỹ Thuật Điện Tử 2",
    "PhoneNumber": "0869243748",
}
print(
    sinhvien["hoVaten"]
)  # Có thể truy cập các mục của từ điển bằng cách đặt tên khóa của nó bên trong dấu ngoặc vuông
print(sinhvien)
x = sinhvien["Malop"]
print(x)
y = sinhvien.get("Malop")  # Ngoài ra có thể thông qua hàm: "get("biến cần thêm")"
print(y)


# THAY ĐỔI GIÁ TRỊ:
# Có thể thay đổi giá trị của 1 mặt hàng cụ thể bằng cách tham khảo tên khóa của nó:
sinhvien["Malop"] = "D21CQDK02-N"
print(sinhvien["Malop"])
# Hoặc có thể dùng hàm "update()" sẽ cập nhật từ điển với các mục từ đối số đã cho. 
# Và có thể thay đổi nhiều mã cùng 1 lúc
# Đối số phải là 1 từ điển hoặc 1 đối tượng có thể lặp lại với các cặp khóa: giá trị.
sinhvien.update({"Malop": "D21CQDK02-N", "Khoa": "Điện tử 2"})
print(sinhvien)

# THÊM CÁC MỤC:
# Thêm 1 mục vào từ điển được thực hiện bằng cách sử dụng 1 khóa chỉ mục mới và gán 1 giá trị cho nó
sinhvien["NamHoc"] = 2023
# Hoặc cũng có thể dùng hàm update()
sinhvien.update({"NamSinh": 2003})
print(sinhvien)

# lOẠI BỎ CÁC MỤC
# Dùng hàm "pop()" để xóa các mục khỏi từ điển:
sinhvien.pop("NamHoc")
print(sinhvien)
# Dùng hàm "popitem()" là xóa mục được chèn cuối cùng
sinhvien.popitem()
print(sinhvien)
# Hàm "del" giúp xóa tên mục được chỉ đinh, hoặc toàn bộ tử điển:
del sinhvien["PhoneNumber"]
print(sinhvien)

# Dùng hàm "clear()" để làm trống từ điển:
# sinhvien.clear()
# print(sinhvien)
# Sử dụng vòng lặp: để in tất cả các mục trong từ điển, từng cái một
for x in sinhvien:
    print(x)
# Duyệt các giá trị:
for x in sinhvien.values():
    print(x)
# Duyệt các khóa:
for x in sinhvien.keys():
    print("Kết quả:", x)
# Duyệt các cặp khóa - giá trị:
for x, y in sinhvien.items():
    print("1:", x, y)

"""
x = {"Thanh": 28, "Tú": 10, "Nguyễn": 2003}

for i in x:
    print(i, x[i])
