class Queue:  # Định nghĩa lớp Queue
    def __init__(self):
        # Lần lượt khởi tạo enqueue_stack và dequeue_stack là 1 list rỗng [].
        self.enqueue_stack = []  # Dùng để thêm các phần tử vào
        self.dequeue_stack = []  # Dùng để lấy các phần tử ra

    def enqueue(self, data):  # Định nghĩa phương thức enqueue
        self.enqueue_stack.append(
            data
        )  # Dùng append() để đưa phần tử vào cuối cùng của enqueue_stack

    def dequeue(self):  # Định nghĩa phương thức dequeue()
        # Kiểm tra nếu cả 2 stack đều rỗng thì raise Exception
        # Lưu ý: Khi 2 stack đều rỗng thì không thể thực hiện được enqueue/dequeue
        # Lúc đó sẽ raise Exception để dừng luôn chương trình.
        # Lệnh này thường được dùng để cố ý dừng chương trình khi phát hiện trường hợp ngoại lệ
        # hoặc điều kiện không hợp lệ mà không thể xử lý.
        if len(self.enqueue_stack) == 0 and len(self.dequeue_stack) == 0:
            raise Exception("Stacks are empty...")

        if len(self.dequeue_stack) == 0:  # Kiểm tra nếu dequeue_stack rỗng
            while len(self.enqueue_stack) != 0:
                # Lấy từng phần tử từ enqueue_stack bằng pop() và thêm vào dequeue_stack bằng append()
                self.dequeue_stack.append(self.enqueue_stack.pop())

        return (
            self.dequeue_stack.pop()
        )  # Trả về phần tử đầu tiên của dequeue_stack bằng pop()


if __name__ == "__main__":
    queue = Queue()  # Khởi tạo đối tượng Queue và sử dụng

    queue.enqueue(28)
    queue.enqueue(10)
    queue.enqueue(2003)

    print(queue.dequeue())

    queue.enqueue(2810)

    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())
