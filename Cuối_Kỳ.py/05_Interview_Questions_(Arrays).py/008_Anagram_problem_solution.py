# Định nghĩa hàm is_anagram() để kiểm tra xem 2 chuỗi có phải là anagram của nhau hay không
def is_anagram(str1, str2):
    # Kiểm tra độ dài 2 chuỗi, nếu khác nhau thì trả về False luôn
    if len(str1) != len(str2):
        return False

    # Sắp xếp 2 chuỗi theo thứ tự từ điển bằng hàm sorted()
    str1 = sorted(str1)
    str2 = sorted(str2)
    # In ra 2 chuỗi đã sắp xếp để kiểm tra
    print(str1)
    print(str2)

    for i in range(len(str1)):
        # Duyệt qua từng phần tử của 2 chuỗi, nếu có phần tử nào khác nhau thì trả về False
        if str1[i] != str2[i]:
            return False
    # Nếu duyệt hết mà không có phần tử nào khác nhau, tức 2 chuỗi là anagram, trả về True
    return True


if __name__ == "__main__":
    # Khởi tạo 2 list s1 và s2 chứa các ký tự giống nhau nhưng xáo trộn thứ tự
    s1 = ["t", "h", "a", "n", "h", "t", "u"]
    s2 = ["u", "t", "h", "n", "a", "h", "t"]

    print(is_anagram(s1, s2))  # Cuối cùng là gọi hàm is_anagram() để kiểm tra kết quả
