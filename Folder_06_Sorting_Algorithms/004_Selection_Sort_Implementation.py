# Định nghĩa hàm selection_sort() có tham số là list cần sắp xếp.
def selectionsort(A):
    n = len(A)  # Tính độ dài list n = len(list).
    for i in range(n - 1):  # Dùng vòng lặp for i trong range(n-1) để duyệt các vị trí.
        position = i  # Dùng biến position để lưu vị trí phần tử nhỏ nhất.
        # Dùng vòng lặp: for j in range(i+1, n) để tìm phần tử nhỏ hơn. Nếu tìm thấy thì gán position = j.
        for j in range(i + 1, n):
            if A[j] < A[position]:
                position = j
        # Sau khi tìm được phần tử nhỏ nhất, hoán đổi với phần tử tại vị trí i.
        temp = A[i]  # Lưu trữ giá trị của phần tử hiện tại vào biến tạm thời temp
        A[i] = A[position]  # Gán giá trị của phần tử nhỏ nhất vào vị trí hiện tại
        A[
            position
        ] = temp  # Gán giá trị ban đầu của phần tử hiện tại vào vị trí của phần tử nhỏ nhất


# Gọi hàm selection_sort() cần sắp xếp để kiểm tra kết quả.
A = [2, 8, 28, 10, 20, 3, 2003]
print("Original Array:", A)
selectionsort(A)
print("Sorted Array:", A)
