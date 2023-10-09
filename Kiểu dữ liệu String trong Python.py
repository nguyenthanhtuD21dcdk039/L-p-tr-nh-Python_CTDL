# Trong string chúng ta có thể cộng chuỗi lại với nhau
# For example
a = "Thanh Tú"
b = "I love you"
c = "Hoa Hiền"
d = a + " " + b + " " + c  # khoảng trắng giúp ngăn cách các Chuỗi
print(d)

# Tạo chuỗi nhiều dòng
chuoi_nhieu_dong = """
Thanh Tú
Hoa Hiền
"""
print(chuoi_nhieu_dong)

# Lặp lại chuỗi
Nói_yêu = "I miss you so much\n"
Anh_nhớ_em = Nói_yêu * 10
print(Anh_nhớ_em)

# Kiểm tra chuỗi này có nằm bên trong chuỗi khác hay không: Sử dụng từ khóa là "in"
chuoi_1 = "Thanh Tú"
chuoi_2 = "Hoa Hiền"
chuoi_3 = "Thanh Tú I love you Hoa Hiền"
if chuoi_1 in chuoi_3:
    print("Chuỗi 1 là chuỗi con của chuỗi 3")
else:
    print("Chuỗi 1 không phải là chuỗi con của chuỗi 3")

a = input("Nhập vào chuỗi bất kỳ: ")
b = input("Nhập vào chuỗi thứ 2 bất kỳ: ")
c = input("Nhập vào chuỗi thứ 3 bất kỳ: ")

if a in c:
    print("a là chuỗi con của c")
else:
    print("a không phải là chuỗi con của c")

if b in c:
    print("b là chuỗi con của c")
else:
    print("b không phải là chuỗi con của c")

# Viết hoa chữ cái đầu của chuỗi: Dùng câu lệnh "str.capitalize"
a = "i miss you, i miss you so much!"
a = str.capitalize(a)
print(a)

# Viết hoa toàn bộ chuỗi: Dung câu lệnh "str.upper"
a = str.upper(a)  # hoặc có thể dùng "s.upper"
print(a)

# Viết thường toàn bộ chuỗi: Dùng câu lệnh "str.lower"
a = str.lower(a)
print(a)

# Tìm và đếm số lượng chuỗi con
a = "Nguyễn Thanh Tú 28/10/2003 and Hoa Thị Thu Hiền 3/02/2003 !"
print(
    a.find("Nguyễn Thanh Tú")
)  # Nếu có kết quả sẽ trả về đúng vị trí ban đầu (Dùng hàm [find])
print(a.find("Hoa Thị Thu Hiền"))  # Nếu không thì kết quả trả về bằng (-1)
print(a.find("I miss you so much"))  # Đây là tìm kiếm xem có chuỗi con không

print(a.count("Thanh Tú"))  # Đếm số lượng: Dùng hàm (count)

# Thay thế chuỗi: Dùng lệnh (replace)
a = a.replace("and", "I love you")
print(a)

# Cắt chuỗi thành một list: Dùng hàm (split)
a = a.split(" ")
print(a)

# Lấy một chuỗi con
print(a[0:12])
