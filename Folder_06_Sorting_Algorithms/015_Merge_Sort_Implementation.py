# Giới thiệu hàm merge_sort với 3 tham số: mảng a, chỉ số left và chỉ số right
def mergesort(A, left, right):
    # Kiểm tra điều kiện dừng của đệ quy: Nếu chỉ còn một phần tử hoặc không có phần tử nào để sắp xếp (left >= right), thoát.
    if left < right:  # Nếu left < right thì
        mid = (left + right) // 2  # Tính chỉ số mid = (left + right) // 2
        mergesort(A, left, mid)  # Gọi đệ quy hàm merge_sort cho nửa bên trái của mảng
        mergesort(
            A, mid + 1, right
        )  # Gọi đệ quy hàm merge_sort cho nửa bên phải của mảng
        merge(A, left, mid, right)  # Gọi hàm merge để trộn 2 nửa đã sắp xếp


# Định nghĩa hàm merge với 4 tham số tương tự, dùng để trộn 2 mảng con đã sắp xếp
def merge(A, left, mid, right):
    # Khai báo các chỉ số i, j, k
    i = left  # Chỉ số bắt đầu của mảng con trái.
    j = mid + 1  # Chỉ số bắt đầu của mảng con phải.
    k = left  # Chỉ số bắt đầu của mảng kết quả.
    B = [0] * (right + 1)  # Tạo mảng tạm B[] để lưu kết quả trộn
    # Dùng vòng lặp so sánh và lưu các phần tử vào B[]
    while i <= mid and j <= right:
        if A[i] < A[j]:  # Phần tử của mảng con trái nhỏ hơn, thêm vào mảng kết quả.
            B[k] = A[i]
            i = i + 1
        else:
            B[k] = A[j]  # Phần tử của mảng con phải bằng, thêm vào mảng kết quả.
            j = j + 1
        k = k + 1
    # Sao chép các phần tử còn lại của mảng con trái (nếu còn).
    while i <= mid:
        B[k] = A[i]
        i = i + 1
        k = k + 1
    # Sao chép các phần tử còn lại của mảng con phải (nếu còn).
    while j <= right:
        B[k] = A[j]
        j = j + 1
        k = k + 1
    for x in range(left, right + 1):
        A[x] = B[x]  # Và sao chép B[] vào mảng a[] ban đầu


A = [2, 8, 28, 10, 20, 3, 2003]
print("Original Array", A)
mergesort(A, 0, len(A) - 1)
print("Sorted Array:", A)  # In ra list ban đầu và list đã sắp xếp để kiểm tra kết quả
