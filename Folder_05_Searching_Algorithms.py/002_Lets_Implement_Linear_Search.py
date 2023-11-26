def linearsearch(
    A, key
):  # Định nghĩa hàm linear_search() có 2 tham số là mảng a[] và giá trị cần tìm key
    index = 0  # Khai báo biến index = 0
    while index < len(A):  # Sử dụng vòng lặp while duyệt mảng đến khi index >= len(a)
        if (
            A[index] == key
        ):  # Trong vòng lặp nếu if kiểm tra a[index] == key thì trả về index
            return index
        index = index + 1
    return -1  # Nếu không tìm thấy thì trả về -1


A = [84, 21, 47, 96, 15]
found = linearsearch(
    A, 100
)  # Gọi hàm linear_search() với mảng trên và các giá trị key khác nhau
print("Result: ", found)  # In kết quả ra màn hình
