# Định nghĩa hàm binary_search_recursive() có 4 tham số: list A[], key, left index l, right index r
def binarysearch_recursive(A, key, l, r):
    if l > r:  # Kiểm tra điều kiện dừng if l > r thì trả về -1
        return -1
    else:
        mid = (l + r) // 2  # Tính chỉ số mid = (l + r) // 2
        if key == A[mid]:  # Nếu A[mid] == key thì trả về mid
            return mid
        elif key < A[mid]:  # Nếu A[mid] > key thì gọi đệ quy với l, mid-1
            return binarysearch_recursive(A, key, l, mid - 1)
        elif key > A[mid]:  # Ngược lại thì gọi đệ quy với mid+1, r
            return binarysearch_recursive(A, key, mid + 1, r)


A = [15, 21, 47, 84, 96]
# Gọi hàm binary_search_recursive() với mảng trên và các giá trị key cần tìm
found = binarysearch_recursive(A, 28, 0, 4)
print("Result: ", found)  # In ra kết quả
