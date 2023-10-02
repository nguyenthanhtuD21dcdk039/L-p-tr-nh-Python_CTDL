"""
Toán tử điều kiện (toán tử ba ngôi) trong lập trình Python
Cú pháp
[Trả về khi ĐK đúng] if [Điều Kiện] else [Trả về khi ĐK sai]
$$$$Chú ý: Đây không phải câu lệnh (if-Nếu; else-Ngược lại)
"""
# x = "Đúng" if (5 > 3) else "Sai"
# print(x)
x = input("Nhập vào giá trị của x = ")
x = float(x)
Kq = "Chẵn" if (x % 2 == 0) else "Lẻ"
print(x, "Là số", Kq)

a = float(input("Nhập vào giá trị của a = "))
b = float(input("Nhập vào giá trị của b = "))
x = (
    "Giá trị {0} > {1} là Kết quả Đúng".format(a, b)
    if (a > b)
    else "Giá trị {0} < {1} là Kết quả Sai".format(a, b)
)

print(x)
