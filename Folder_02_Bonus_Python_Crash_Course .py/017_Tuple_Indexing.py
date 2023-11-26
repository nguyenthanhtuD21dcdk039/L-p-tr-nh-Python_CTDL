"""
Tuple là một chuỗi các phần tử có thứ tự như một List. Sự khác biệt duy nhất 
là bộ giá trị là các hằng số. Tuples một khi đc tạo ra thì giá trị của nó ko thể sữa đổi
Tuples được sử dụng để bảo vệ dữ liệu và thường nhanh hơn danh sách vì chúng ko thể thay đổi động
Được định nghĩa trong dấu ngoặc đơn(), các mục đc phân tách bằng dấu phẩy
"""
Gioitinh = ("Nam", "Nữ")
lopHoc = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)
TraiCay = ("Táo", "Ổi", "Cam", "Soài", "Dưa hấu", "Chuối", "Mận")
# Trong tuples có thể truy cập nhiều mục bằng cách tham khảo số chỉ mục, bên trong dấu ngoặc vuông:
print(Gioitinh[0])
print(TraiCay[0:3])  # Lưu ý giá trị phần tử tuple ko thể thay đổi
# và trong tuple chúng ta cũng có thể duyệt từng phần tử bằng vòng lặp
for x in TraiCay:
    print(x)
# Bạn cũng có thể sử dụng toán tử in để kiểm tra xem phần từ có tồn tại trong bộ tuple hay ko
print("Táo" in TraiCay)  # Và kết quả trả về là True and False
print("Na" in TraiCay)
# Cũng giống như lists, tuple cũng sử dụng hàm "len" để đếm số lượng phần tử
a = len(TraiCay)
print(a)
# Ngoài ra tương tự đếm số lượng xuất hiện là sử dụng hàm "count"
print(TraiCay.count("Soài"))
print(TraiCay.count("Na"))
