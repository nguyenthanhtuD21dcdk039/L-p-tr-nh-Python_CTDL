# Định nghĩa hàm find_duplicates() để tìm các phần tử trùng lặp trong mảng nums
def find_duplicates(nums):
    for num in nums:  # Duyệt qua từng phần tử num trong mảng nums
        # Sử dụng giá trị tuyệt đối abs(num) để truy cập vào vị trí tương ứng trong mảng
        if nums[abs(num)] >= 0:  # Nếu giá trị tại vị trí x >= 0
            nums[abs(num)] = -nums[
                abs(num)
            ]  # Gán giá trị âm -nums[abs(num)] vào vị trí x
        else:  # Ngược lại nếu < 0
            # Nghĩa là trước đó đã đánh dấu âm => trùng lặp
            print(
                "Repetition found: %s" % str(abs(num))
            )  # In ra thông báo tìm thấy phần tử trùng abs(num)


if __name__ == "__main__":
    n = [2, 6, 5, 5, 4, 4, 2]
    find_duplicates(n)  # Gọi lại hàm
