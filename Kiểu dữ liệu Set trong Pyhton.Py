"""
Set là một trong 4 kiểu dữ liệu tích hợp sẵn trong Python dùng để lưu trữ các tập hợp dữ liệu, 3 kiểu còn lại là List, Tuple và Dictionary, tất cả đều có chất lượng và cách sử dụng khác nhau
Set là tập hợp ko có thứ tự, giá trị ko đc trùng nhau, ko thể thay đổi và ko đc lặp chỉ mục. 
Lưu ý: các mục set là ko thể thay đổi, nhưng bạn có thể xóa các mục và thêm các mục mới.
Và set sử dụng cặp ngoặc {}
"""
# Tạo mới
monHoc = {"Toán", "Lý", "Hóa"}
print(monHoc)

# Duyệt danh sách phần tử trong Set
for x in monHoc:
    print(x)

# Thêm mới phần tử vào bên trong Set: Dùng lệnh "add"
monHoc.add("Tiếng Anh")
print(monHoc)

# THêm một tập hợp khác hoặc một list khác: Dùng lệnh "update"
# Sử dụng "update"
hocThem = {"Sử", "Địa", "Sinh"}
monHoc.update(hocThem)
print(monHoc)
"""
# Xóa phần tử
# Sử dụng phương thức "remove": Nếu phần tử ko tồn tại sẽ phát sinh lỗi
monHoc.remove("Ngữ Văn")
print(monHoc)
# Sử dụng phương thức "discard": Nếu phần tử ko tồn tại sẽ ko phát sinh lỗi
monHoc.discard("Ngữ Văn")
print(monHoc)
"""
# Loại bỏ phần tử đầu tiên bằng phương thức "pop"
monHoc.pop()
print(monHoc)
# Làm rỗng tập hợp bằng phương thức "clear"
monHoc.clear()
print(monHoc)
# Xóa bỏ tập hợp bằng từ khóa "del"
del monHoc
print(monHoc)
