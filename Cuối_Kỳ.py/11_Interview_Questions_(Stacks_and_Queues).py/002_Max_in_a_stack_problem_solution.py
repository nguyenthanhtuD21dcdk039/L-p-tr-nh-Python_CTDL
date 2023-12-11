class MaxStack:  # Định nghĩa class MaxStack
    def __init__(self):  # Hàm khởi tạo init()
        self.main_stack = (
            []
        )  # Khởi tạo thuộc tính main_stack là 1 list rỗng [] để lưu tất cả phần tử
        self.max_stack = (
            []
        )  # Khởi tạo thuộc tính max_stack là 1 list rỗng [] để lưu các phần tử lớn nhất

    def push(self, data):  # Định nghĩa phương thức push
        self.main_stack.append(data)  # Thêm phần tử vào main_stack
        if (
            len(self.main_stack) == 1
        ):  # Kiểm tra nếu main_stack mới có 1 phần tử thì gán luôn cho max_stack
            self.max_stack.append(data)
            return

        if (
            data > self.max_stack[-1]
        ):  # Nếu phần tử thêm vào > phần tử cuối cùng trong max_stack
            self.max_stack.append(data)  # Thêm vào max_stack
        else:  # Ngược lại thêm phần tử cuối cùng đó vào max_stack
            self.max_stack.append(self.max_stack[-1])

    def pop(self):  # Định nghĩa phương thức pop
        self.max_stack.pop()  # Xóa phần tử cuối cùng của max_stack bằng phương thức pop()
        return (
            self.main_stack.pop()
        )  # Xóa phần tử cuối cùng của main_stack bằng phương thức pop()
        # Vậy là đã đồng bộ xóa 1 phần tử ở cả 2 stack

    def get_max_item(self):
        return (
            self.max_stack.pop()
        )  # Lấy phần tử cuối cùng của max_stack bằng pop() (phần tử lớn nhất)


if __name__ == "__main__":
    max_stack = MaxStack()  # Khởi tạo đối tượng MaxStack và sử dụng

    max_stack.push(2)
    max_stack.push(8)
    max_stack.push(28)
    max_stack.push(10)
    max_stack.push(2003)

    print(max_stack.get_max_item())
