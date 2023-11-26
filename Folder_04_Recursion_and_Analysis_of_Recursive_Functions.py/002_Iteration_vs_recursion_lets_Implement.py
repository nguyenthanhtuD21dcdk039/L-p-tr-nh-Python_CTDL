"""
# Hàm được giải bằng cách lặp
def calculate_itr(n): # def từ khóa để định dạng hàm
    while n > 0: # Hàm được sử dụng vòng lặp While để lặp
        k = n**2
        print(k)
        n = n - 1 # Và giảm n sau mỗi lần lặp

calculate_itr(4)
"""


# Hàm đệ quy sử dụng gọi chính nó và điều kiện dừng.
def calculate_rec(n):
    if n > 0:  # if Nếu điều kiện này đúng (nghĩa là n còn lớn hơn 0)
        k = n**2
        print(k)
        calculate_rec(n - 1)  # Gọi lại hàm với n-1, cho đến khi N <= 0


calculate_rec(4)
