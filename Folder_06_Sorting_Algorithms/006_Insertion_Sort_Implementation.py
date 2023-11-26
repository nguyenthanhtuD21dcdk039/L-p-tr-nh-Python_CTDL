# Định nghĩa hàm insertion_sort() với tham số là list cần sắp xếp
def insertionsort(A):
    n = len(A)  # Lấy độ dài của danh sách
    # Dùng vòng lặp for duyệt từ phần tử thứ 2 đến cuối list
    # Lấy phần tử tại vị trí i vào biến key
    for i in range(1, n):
        cvalue = A[i]  # Lưu trữ giá trị của phần tử hiện tại
        position = i  # Lưu trữ vị trí của phần tử hiện tại
        # Dùng vòng lặp while để dịch chuyển các phần tử lớn hơn key sang phải
        # Gán key vào đúng vị trí sao cho các phần tử bên trái nhỏ hơn key
        while position > 0 and A[position - 1] > cvalue:
            # Kiểm tra nếu phần tử tại vị trí trước đó (position - 1) lớn hơn giá trị hiện tại (cvalue)
            A[position] = A[position - 1]  # Di chuyển phần tử trước đó lên một vị trí
            position = position - 1  # Di chuyển vị trí hiện tại lên một vị trí

        # Khi vòng lặp while kết thúc, vị trí 'position' là vị trí thích hợp cho giá trị hiện tại (cvalue)
        A[position] = cvalue  # Gán giá trị hiện tại vào vị trí thích hợp


# In ra list ban đầu và selection_sort() đã sắp xếp để kiểm tra kết quả
A = [2, 8, 28, 10, 20, 3, 2003]
print("Original Array:", A)
insertionsort(A)
print("Sorted Array:", A)
