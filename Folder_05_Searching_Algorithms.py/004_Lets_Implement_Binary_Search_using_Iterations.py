# Định nghĩa hàm binary_search_iterative() có 2 tham số là list a[] và giá trị cần tìm key
def binarysearch_iterative(A, key):
    l = 0  # Khai báo biến l = 0, r = len(a) - 1
    r = len(A) - 1
    while l <= r:  # Sử dụng vòng lặp while l <= r
        mid = (l + r) // 2  # Tính chỉ số mid = (l + r) // 2
        if key == A[mid]:  # Nếu A[mid] == key thì trả về mid
            return mid
        elif key < A[mid]:  # Nếu A[mid] > key thì r = mid - 1, ngược lại l = mid + 1
            r = mid - 1
        elif key > A[mid]:
            l = mid + 1
    return -1  # Nếu không tìm thấy thì trả về -1


A = [15, 21, 47, 84, 96]
# Gọi hàm binary_search_iterative() với mảng trên và các giá trị key khác nhau
found = binarysearch_iterative(A, 28)
print("Result:", found)  # In ra kết quả
