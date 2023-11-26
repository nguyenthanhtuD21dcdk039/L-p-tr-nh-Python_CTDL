# Định nghĩa hàm bubble_sort() với tham số là list cần sắp xếp
def bubblesort(A):
    n = len(A)  # Lấy độ dài của danh sách
    for passes in range(
        n - 1, 0, -1
    ):  # Dùng vòng lặp for bên ngoài duyệt số lần so sánh
        # Vòng lặp for bên trong duyệt từ đầu đến vị trí kết thúc so sánh trong mỗi lần duyệt
        for i in range(passes):
            if (
                A[i] > A[i + 1]
            ):  # So sánh 2 phần tử liên tiếp, nếu a[i] > a[i+1] thì hoán đổi chỗ
                temp = A[
                    i
                ]  # Sử dụng biến tạm thời để lưu trữ giá trị của phần tử hiện tại
                A[i] = A[i + 1]  # Gán phần tử kế bên vào vị trí hiện tại
                A[i + 1] = temp  # Gán giá trị từ biến tạm thời vào vị trí kế bên


# In ra list ban đầu và bubble_sort() đã sắp xếp để kiểm tra kết quả
A = [2, 8, 28, 10, 20, 3, 2003]
print("Original Array:", A)
bubblesort(A)
print("Sorted Array:", A)
