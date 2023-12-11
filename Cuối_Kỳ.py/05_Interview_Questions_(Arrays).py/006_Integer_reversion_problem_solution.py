# Định nghĩa hàm reverse_integer() với tham số n cần đảo ngược
def reverse_integer(n):
    reversed_integer = 0  # Khai báo biến reversed_integer để lưu kết quả đảo ngược

    # Sử dụng vòng lặp while để lấy từng chữ số của n
    while n > 0:
        remainder = (
            n % 10
        )  # Lấy phần dư remainder của n chia 10 để lấy ra chữ số cuối cùng
        reversed_integer = reversed_integer * 10 + remainder  # Để đảo ngược dần
        n = n // 10  # Dịch chữ số của n sang phải bằng cách chia nguyên // 10
    # Sau khi đã duyệt hết các chữ số của n, reversed_integer chứa giá trị đã đảo ngược
    return reversed_integer


if __name__ == "__main__":
    print(reverse_integer(123456789))
