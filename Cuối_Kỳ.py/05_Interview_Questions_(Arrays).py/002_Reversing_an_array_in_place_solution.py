# Định nghĩa hàm reverse() có tham số truyền vào là nums. Dùng để đảo ngược thứ tự các phần tử trong nums
# theo nguyên lý hoán đổi vị trí phần tử đầu và phần tử cuối,
# rồi dần dần hoán đổi vào phần tử kế tiếp.
def reverse(nums):
    # Định nghĩa chỉ số bắt đầu và chỉ số kết thúc của mảng nums
    start_index = 0
    end_index = len(nums) - 1
    # Vòng lặp while sẽ lặp cho đến khi hoán đổi hết các phần tử
    while end_index > start_index:
        # Trong mỗi vòng lặp sẽ hoán đổi giá trị của phần tử tại vị trí start_index và end_index
        nums[start_index], nums[end_index] = nums[end_index], nums[start_index]
        # Sau đó tăng start_index lên 1 và giảm end_index xuống 1 để tiếp tục hoán đổi các phần tử kế tiếp
        start_index = start_index + 1
        end_index = end_index - 1


if __name__ == "__main__":
    n = [2, 8, 28, 10, 2003]  # Khởi tạo mảng n
    reverse(n)  # Gọi hàm reverse(n) để đảo ngược mảng n
    print(n)  # In ra mảng sau khi đã đảo ngược
