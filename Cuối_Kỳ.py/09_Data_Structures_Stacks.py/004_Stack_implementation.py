class Stack:  # Định nghĩa class Stack
    def __init__(self):  # Định nghĩa hàm khởi tạo init()
        self.stack = (
            []
        )  # Khởi tạo self.stack là một list trống, để lưu trữ các phần tử của stack

    def push(self, data):  # Định nghĩa phương thức push. Dùng để thêm phần tử vào stack
        self.stack.append(
            data
        )  # Sử dụng phương thức append() để thêm phần tử vào CUỐI của list.
        # Tương ứng việc thêm vào ĐẦU của stack

    def pop(
        self,
    ):  # Định nghĩa phương thức pop. Dùng để lấy PHẦN TỬ ĐẦU stack ra và xóa đi
        if self.stack_size() < 1:  # Kiểm tra nếu kích thước stack = 0
            return -1  # Trả về -1

        data = self.stack[
            -1
        ]  # Lấy phần tử cuối cùng của list (tương ứng phần tử ĐẦU stack) gán vào data
        del self.stack[
            -1
        ]  # Xóa phần tử cuối cùng khỏi list. Tương ứng xóa phần tử ĐẦU stack
        return data  # Trả về phần tử đã lấy ra được đã lưu trong data

    def peek(
        self,
    ):  # Định nghĩa phương thức peek(). Dùng để lấy phần tử đầu stack mà KHÔNG XÓA
        return self.stack[
            -1
        ]  # Trả về phần tử cuối cùng của list mà không làm thay đổi stack

    def is_empty(
        self,
    ):  # Định nghĩa phương thức is_empty(). Dùng để KIỂM TRA stack có rỗng hay không
        return self.stack == []  # So sánh self.stack với list rỗng []
        # Nếu bằng nhau (stack rỗng) thì trả về True Và ngược lại.

    def stack_size(
        self,
    ):  # Định nghĩa stack_size(). Dùng để lấy KÍCH THƯỚC (số lượng phần tử) của stack
        return len(
            self.stack
        )  # Để lấy độ dài của list tương ứng kích thước. Và trả về độ dài đó


stack = Stack()  # Khởi tạo Stack và sử dụng các phương thức đã định nghĩa
stack.push(1)  # Thêm 1 vào stack
stack.push(2)  # Thêm 2 vào stack
stack.push(3)  # Thêm 3 vào stack
print("Size : %d" % stack.stack_size())
print("Popped item: %d" % stack.pop())
print("Size : %d" % stack.stack_size())
print("Popped item: %d" % stack.peek())
print("Size : %d" % stack.stack_size())
print("Popped item: %d" % stack.pop())
print("Popped item: %d" % stack.pop())
print("Popped item: %d" % stack.pop())
