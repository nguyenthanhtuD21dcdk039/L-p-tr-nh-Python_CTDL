class Queue:  # Định nghĩa lớp Queue
    def __init__(self):
        self.stack = (
            []
        )  # Khởi tạo thuộc tính self.stack là 1 list rỗng [] để lưu các phần tử

    def enqueue(self, data):  # Định nghĩa phương thức enqueue
        self.stack.append(data)  # Dùng append() để đưa phần tử vào cuối stack

    def dequeue(self):
        if len(self.stack) == 1:  # Kiểm tra nếu stack chỉ có 1 phần tử thì pop luôn
            return self.stack.pop()  # Pop ra 1 phần tử và lưu vào item

        item = self.stack.pop()  # Gọi đệ quy hàm dequeue()

        dequeued_item = self.dequeue()  #  Đặt lại phần tử vừa pop ra ban nãy

        self.stack.append(item)
        return dequeued_item  # Trả về phần tử đã được dequeue ở lần đệ quy trước


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
