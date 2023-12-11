class Queue:  # Định nghĩa lớp Queue
    def __init__(self):  # Định nghĩa hàm khởi tạo init()
        self.queue = (
            []
        )  # Khởi tạo thuộc tính self.queue là 1 list rỗng [].Lưu trữ các phần tử trong queue

    def is_empty(
        self,
    ):  # Định nghĩa phương thức is_empty(). Dùng để kiểm tra queue có rỗng hay không
        return (
            self.queue == []
        )  # So sánh self.queue với list rỗng []. Trả về True nếu rỗng, và ngược lại

    def enqueue(
        self, data
    ):  # Định nghĩa phương thức enqueue(). Dùng để thêm phần tử vào CUỐI queue
        self.queue.append(
            data
        )  # Sử dụng phương thức append() để thêm phần tử data vào cuối của list
        # Tương ứng việc thêm vào cuối queue

    def dequeue(
        self,
    ):  # Định nghĩa phương thức dequeue(). Dùng để lấy PHẦN TỬ ĐẦU queue ra và xóa đi
        if self.size_queue() != 0:  # Kiểm tra nếu kích thước queue = 0 thì trả về -1
            data = self.queue[0]  # Gán phần tử đầu tiên của list vào biến data
            del self.queue[
                0
            ]  # Dùng del để xóa phần tử đầu tiên của list. Tương ứng xóa phần tử ĐẦU queue
            return data  # Trả về phần tử đã lấy ra được đã lưu trong data
        else:
            return -1  # Ngược lại trả về -1

    def peek(
        self,
    ):  # Định nghĩa phương thức peek(). Dùng để LẤY giá trị phần tử đầu nhưng KHÔNG XÓA
        return self.queue[
            0
        ]  # Trả về phần tử đầu tiên của list mà không làm thay đổi queue

    def size_queue(
        self,
    ):  # Định nghĩa phương thức size_queue(). Dùng để lấy KÍCH THƯỚC (số lượng phần tử) của queue
        return len(
            self.queue
        )  # Sử dụng hàm len() để lấy độ dài của list. Tương ứng kích thước của queue và trả về


queue = Queue()  # Khởi tạo đối tượng Queue và sử dụng
queue.enqueue(28)
queue.enqueue(10)
queue.enqueue(2003)
print("Size: %d" % queue.size_queue())
print("Dequeue: %d" % queue.dequeue())
print("Dequeue: %d" % queue.dequeue())
print("Dequeue: %d" % queue.dequeue())
print("Dequeue: %d" % queue.dequeue())
print("Size: %d" % queue.size_queue())
