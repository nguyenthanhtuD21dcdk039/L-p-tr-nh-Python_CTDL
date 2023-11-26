# Các bước implement hàm tính giai thừa đệ quy factorial_rec()
def factorial_rec(n):  # Định nghĩa hàm đệ quy factorial_rec() có tham số là n
    if n == 0:  # Kiểm tra điều kiện if nếu n == 0, trả về 1
        return 1
    return factorial_rec(n - 1) * n  # Gọi đệ quy factorial_rec(n-1) * n


num = input("Enter Number: ")  # Nhập input từ người dùng và ép kiểu thành int
n = int(num)
print(
    factorial_rec(n)
)  # Gọi hàm factorial_rec() với tham số là giá trị nhập vào và in ra hết quả
