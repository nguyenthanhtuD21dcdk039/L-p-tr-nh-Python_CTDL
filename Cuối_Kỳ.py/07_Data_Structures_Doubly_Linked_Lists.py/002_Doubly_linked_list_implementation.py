class Node:  # Khai báo class Node
    def __init__(self, data):  # Hàm khởi tạo Node, có tham số là data
        self.data = data  # Gán giá trị data vào thuộc tính self.data của Node
        self.next = None  # Khởi tạo thuộc tính self.next và gán = None (Con trỏ trỏ tới Node kế tiếp)
        self.previous = None  # Khởi tạo thuộc tính self.previous, gán = None (Con trỏ trỏ tới Node phía trước)


class DoublyLinkedList:  # Khai báo Class DoublyLinkedList
    def __init__(self):  # Khởi tạo hàm
        self.head = None  # Khởi tạo thuộc tính self.head và gán ban đầu = None
        self.tail = None  # Khởi tạo thuộc tính self.tail và gán ban đầu = None

    def insert(self, data):
        new_node = Node(data)  # Khởi tạo 1 Node mới, truyền vào data cần chèn

        if (
            self.head is None
        ):  #  Kiểm tra nếu self.head = None (nghĩa là danh sách ban đầu rỗng)
            self.head = new_node  # Gán self.head = Node mới
            self.tail = new_node  # Gán self.tail = Node mới (Lúc này head và tail cùng trỏ tới Node mới)
        else:  # Nếu danh sách đã có Node
            new_node.previous = self.tail  # Cho Node mới trỏ ngược lại tail cũ
            self.tail.next = new_node  # Cho tail cũ trỏ tới Node mới
            self.tail = new_node  # Cuối cùng cập nhật lại self.tail = Node mới

    def traverse_forward(self):  # Khởi tạo hàm duyệt từ đầu đến cuối
        actual_node = self.head  # Bắt đầu duyệt từ node đầu tiên = head)

        while actual_node is not None:
            print(
                "%d" % actual_node.data
            )  # In ra màn hình giá trị data của node hiện tại
            actual_node = (
                actual_node.next
            )  # Chuyển sang node liền kề phía sau của node hiện tại

    # Quá trình này cứ lặp lại cho đến khi actual_node = None, tức đã duyệt hết danh sách các node.

    def traverse_backward(self):  # Khởi tạo hàm duyệt từ cuối về đầu
        actual_node = self.tail  # Bắt đầu từ node cuối cùng = tail

        while actual_node is not None:
            print("%d" % actual_node.data)  # In ra data của node đang duyệt
            actual_node = (
                actual_node.previous
            )  # Chuyển ngược lại sang node phía trước đó


# Cứ thế duyệt ngược dần về đầu danh sách cho đến khi gặp actual_node = None

if __name__ == "__main__":
    linked_list = DoublyLinkedList()
    linked_list.insert(28)
    linked_list.insert(10)
    linked_list.insert(2003)

    linked_list.traverse_forward()
    print("----------")
    linked_list.traverse_backward()
