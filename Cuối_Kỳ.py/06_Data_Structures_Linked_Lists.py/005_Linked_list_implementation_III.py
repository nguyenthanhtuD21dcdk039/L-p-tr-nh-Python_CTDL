# Định nghĩa lớp Node
class Node:
    def __init__(self, data):  # Hàm khởi tạo, nhận tham số data
        self.data = data  # Gán data vào thuộc tính self.data
        self.nextNode = None  # Khởi tạo thuộc tính self.nextNode = None (con trỏ trỏ tới node kế tiếp)


# Định nghĩa lớp LinkedList
class LinkedList:
    def __init__(self):
        self.head = None  # Node đầu tiên của danh sách
        self.num0fNodes = (
            0  # Đếm số node. Vì mới khởi tạo nên danh sách không có node nào!
        )

    def insert_start(self, data):  # insert_start: chèn 1 node vào đầu danh sách
        self.num0fNodes = self.num0fNodes + 1  # Tăng biến đếm numOfNodes lên 1
        new_node = Node(data)  # Khởi tạo node mới với data truyền vào

        if not self.head:  # Kiểm tra nếu danh sách chưa có node nào
            self.head = new_node  # Gán node mới thành head
        else:
            new_node.nextNode = self.head  #  Nối nextNode của node mới = head cũ
            self.head = new_node  # Cập nhật node mới thành head

    def insert_end(self, data):
        self.num0fNodes = self.num0fNodes + 1  # Tăng biến đếm numOfNodes lên 1
        new_node = Node(data)  # Khởi tạo node mới

        actual_node = self.head  # Gán actual_node = head để duyệt

        while (
            actual_node.nextNode is not None
        ):  # Vòng lặp duyệt từ đầu đến cuối danh sách
            actual_node = actual_node.nextNode  # Cập nhật actual_node = node kế tiếp
        # Khi thoát vòng lặp, actual_node = node cuối => Gán nextNode của node cuối = node mới
        actual_node.nextNode = new_node

    def remove(self, data):
        if self.head is None:  # Nếu linked list rỗng thì thoát luôn
            return

        # Duyệt qua các node với previous_node và actual_node
        actual_node = self.head  # Gán actual_node = head để bắt đầu duyệt từ đầu
        previous_node = None  # Khởi tạo previous_node = None

        # Vòng lặp duyệt danh sách
        while (
            actual_node is not None and actual_node.data != data
        ):  # So sánh data có bằng với giá trị cần xoá hay không
            previous_node = actual_node  # Cập nhật previous_node = node hiện tại
            actual_node = actual_node.nextNode  # Chuyển actual_node sang node tiếp theo

        if actual_node is None:  # Nếu không tìm thấy node cần xoá thì thoát
            return
        # Nếu tìm thấy node cần xoá:
        self.num0fNodes = self.num0fNodes - 1  # Giảm biến đếm node đi 1

        if previous_node is None:  # Kiểm tra xem có phải xoá node đầu hay không
            self.head = actual_node.nextNode  # Nếu phải: gán lại head = node kế tiếp
        else:  # Ngược lại: gán nextNode của previous_node "nhảy qua" node cần xoá
            previous_node.nextNode = actual_node.nextNode

    def size_of_list(self):
        return self.num0fNodes  # Trả về giá trị của biến đếm numOfNodes

    def traverse(self):
        actual_node = self.head  # Gán actual_node = head để bắt đầu duyệt từ đầu

        while actual_node is not None:  #  Vòng lặp duyệt từng node
            print(actual_node.data)  # In ra data của node
            actual_node = actual_node.nextNode  # Chuyển actual_node sang node liền kề


linked_list = LinkedList()
linked_list.insert_start(2)  # Chèn 1 node vào đầu danh sách bằng 2
linked_list.insert_start(8)
linked_list.insert_start(28)
linked_list.insert_start(10)
linked_list.insert_start("Thanh Tú")
linked_list.insert_end(20.03)  # Chèn node vào cuối danh sách bằng 20.03
linked_list.insert_end(2003)

linked_list.traverse()
print("Size: %d " % linked_list.size_of_list())
linked_list.remove("Thanh Tú")
print("Size: %d " % linked_list.size_of_list())
print("----------")
linked_list.traverse()
