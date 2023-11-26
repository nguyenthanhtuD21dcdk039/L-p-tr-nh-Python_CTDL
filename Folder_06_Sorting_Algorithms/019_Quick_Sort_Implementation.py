# Định nghĩa hàm quicksort có 3 tham số: mảng a, chỉ số trái low và chỉ số phải high
def quicksort(A, low, high):
    if low < high:  # Kiểm tra điều kiện low < high
        # Gọi hàm partition() để phân hoạch mảng
        # Hàm này cũng có 3 tham số tương tự và trả về chỉ số của pivot sau khi phân hoạch
        pi = partition(A, low, high)
        # Gọi đệ quy hàm quicksort lên 2 mảng con bên trái và phải của pivot
        quicksort(A, low, pi - 1)
        quicksort(A, pi + 1, high)


def partition(A, low, high):  # Định nghĩa hàm partition()
    pivot = A[low]  # Chọn phần tử pivot, thường là phần tử đầu tiên
    i = low + 1
    j = high
    # Sử dụng vòng lặp while. Swap phần tử bằng toán tử gán đa biến.
    while True:
        while i <= j and A[i] <= pivot:
            i += 1  # Di chuyển i sang phải để tìm phần tử lớn hơn pivot
        while i <= j and A[j] > pivot:
            j -= 1  # Di chuyển j sang trái để tìm phần tử nhỏ hơn hoặc bằng pivot
        if i <= j:
            A[i], A[j] = A[j], A[i]  # Nếu i và j gặp nhau, đổi chỗ hai phần tử
        else:
            break  # Khi i > j, thoát khỏi vòng lặp
    # Đổi chỗ pivot với phần tử A[j]
    A[low], A[j] = A[j], A[low]
    return j  # Trả về chỉ mục của pivot sau khi đã sắp xếp


A = [2, 8, 28, 10, 20, 3, 2003]
print("Original Array:", A)
quicksort(A, 0, len(A) - 1)  # Gọi hàm quicksort để sắp xếp danh sách
print("Sorted Array:", A)  # In danh sách sau khi sắp xếp
