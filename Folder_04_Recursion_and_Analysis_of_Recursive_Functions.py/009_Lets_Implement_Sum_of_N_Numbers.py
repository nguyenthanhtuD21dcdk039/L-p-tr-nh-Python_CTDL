# Tính tổng N số tự nhiên bằng đệ quy:
def sum_rec(n):  # Định nghĩa hàm đệ quy sum_rec() có tham số là n
    if n == 0:  # Kiểm tra điều kiện if nếu n == 0, trả về 0
        return 0
    return sum_rec(n - 1) + n  # Tiếp tục gọi đệ quy sum_rec(n-1) + n


num = input("Enter Number: ")  # Nhập input từ người dùng và ép kiểu thành int
n = int(num)
print(sum_rec(n))  # Gọi hàm sum_rec() với tham số là giá trị nhập vào và In ra kết quả
