# Tạo list rỗng
Hello = []  # tạo list bằng dấu ngoặc vuông[]
Hello1 = list()  # Cách tạo list thứ 2
print(Hello)
print(Hello1)

# Tạo list có dữ liệu
Such_as = [
    "Thanh",
    "Tu",
    "28",
    "10",
    "2003",
    "!",
]
# List có thể chứa nhiều kiểu dữ liệu khác nhau vừa có thể là số, chữ , ký tự...
print(Such_as)
# List có thứ tự, vị trí các phần tử được đánh dấu bắt đầu từ 0, từ trái sang phải
Name = ["Thanh Tú", "28/10/2003", "Thanh Tú", "28/10/2003", "Nguyễn Thanh Tú"]
print(Name)
print(
    Name[2:4]
)  # Kiểu dữ liệu được in ra màn hình là ở vị trí phần tử 2 và 3 tức (4-1)
print(Name[:])  # In toàn bộ dữ liệu ra màn hình
print(Name[-1])  # In giá trị ngược lại

# Thêm phần tử vào cuối list: Dùng lệnh "append"
Name.append("I love you")
print(Name)

# Chèn phần tử vào list
Name.insert(
    2, "I love you"
)  # Chèn vào list, đầu tiên phải thêm vào vị trí cần khai báo tiếp đến là dữ liệu
print(Name)

# Số lượng phần tử có trong list: Dùng lệnh "len". Và khi tính số lượng phần tử thì đc bắt đầu từ 1
print(len(Name))

# Đếm số lượng phần tử thỏa điều kiện: Dùng lệnh "count"
print("Thanh Tú:", Name.count("Thanh Tú"))
print("I love you:", Name.count("I love you"))
print("Hoa Thị Thu Hiền", Name.count("Hoa Thị Thu Hiền"))
# Xóa phần tử ra khỏi list bằng giá trị: Dùng lệnh "remove"
Name.remove("I love you")
print(Name)
# Kiểm tra xem giá trị có nằm trong list hay không: dùng "in"
if "I love you" in Name:
    Name.remove("I love you")
    print(Name)

# Xóa phần tử ra khỏi list bằng vị trí: Dùng lệnh "pop"
Name.pop(4)
print(Name)

# Đảo ngược list: Dùng lệnh "reverse"
Name.reverse()
print(Name)

# Sắp xếp trong list: Dùng lệnh "sort"
Name.sort()
print(Name)

# Sắp xếp ngược trong list: Dùng lệnh "sort(reverse=True)"
Name.sort(reverse=True)
print(Name)

# Xóa sạch hết trong List: Dùng lệnh "clear"
Name.clear()
print(Name)

# Tính tổng: dùng lệnh "Sum"
