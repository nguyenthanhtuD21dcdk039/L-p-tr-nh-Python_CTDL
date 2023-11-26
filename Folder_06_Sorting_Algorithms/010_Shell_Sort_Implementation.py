def shellsort(A):  # Định nghĩa hàm shell_sort() với tham số là list cần sắp xếp
    n = len(A)  # Lấy độ dài của danh sách
    gap = n // 2  # Khởi tạo biến gap = n//2
    while gap > 0:  # Sử dụng vòng lặp while với điều kiện gap > 0
        i = gap  # Bắt đầu từ vị trí cách gap phần tử
        while i < n:  # Trong vòng lặp, duyệt phần tử từ gap đến cuối list
            temp = A[i]
            j = i - gap
            # So sánh phần tử hiện tại với phần tử cách đó gap, nếu lớn hơn thì hoán đổi
            while j >= 0 and A[j] > temp:
                # Di chuyển phần tử lớn hơn giá trị hiện tại về phía sau khoảng cách gap
                A[j + gap] = A[j]
                j = j - gap
            A[
                j + gap
            ] = temp  # Gán giá trị hiện tại vào vị trí thích hợp sau khi di chuyển
            i = i + 1  # Di chuyển đến phần tử tiếp theo
        gap = gap // 2  # Sau mỗi vòng lặp giảm gap = gap//2


# In ra list ban đầu và shell_sort() đã sắp xếp để kiểm tra kết quả
A = [2, 8, 28, 10, 20, 3, 2003]
print("Original Array:", A)
shellsort(A)
print("Sorted Array:", A)
