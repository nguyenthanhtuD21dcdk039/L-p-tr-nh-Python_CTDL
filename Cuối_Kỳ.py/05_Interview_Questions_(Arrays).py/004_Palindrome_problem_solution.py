# Định nghĩa hàn is_palindrome() nhận vào tham số là chuỗi cần kiểm tra s
def is_palindrome(s):
    original_string = s  # Gán biến original_string = s để lưu lại chuỗi gốc
    reversed_string = reverse(
        s
    )  # Gọi hàm reverse(s) để đảo ngược chuỗi s và gán vào biến reversed_string
    # So sánh 2 chuỗi original_string và reversed_string
    if original_string == reversed_string:
        return True  # Nếu bằng nhau (palindrome) thì trả về True

    return False  # Nếu không bằng thì trả về False


# Hàm reverse(data) định nghĩa cách đảo ngược một chuỗi
def reverse(data):
    data = list(data)  # Chuyển chỗi sang list
    start_index = 0
    end_index = len(data) - 1
    # Vòng lặp while sẽ lặp cho đến khi hoán đổi hết các phần tử
    while end_index > start_index:
        # Trong mỗi vòng lặp sẽ hoán đổi giá trị của phần tử tại vị trí start_index và end_index
        data[start_index], data[end_index] = data[end_index], data[start_index]
        # Sau đó tăng start_index lên 1 và giảm end_index xuống 1 để tiếp tục hoán đổi các phần tử kế tiếp
        start_index = start_index + 1
        end_index = end_index - 1

    return "".join(data)


if __name__ == "__main__":
    print(is_palindrome("TTuTT"))
