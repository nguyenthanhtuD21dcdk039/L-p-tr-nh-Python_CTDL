class Node:  # Khai báo class Node
    def __init__(self, data):  # Hàm khởi tạo Node, có tham số là data
        self.data = data  # Gán giá trị data vào thuộc tính self.data của Node
        self.next_node = None


class LinkedList:  # Khai báo Class LinkedList
    def __init__(self):  # Khởi tạo hàm
        self.head = None  # Khởi tạo thuộc tính self.head và gán ban đầu = None
        self.size = 0

    def get_middle_node(self):
        fast_pointer = (
            self.head
        )  # Khai báo fast_pointer, gán bằng self.head // Bắt đầu từ node đầu tiên (head)
        slow_pointer = (
            self.head
        )  # Khai báo slow_pointer, cũng gán bằng self.head // Bắt đầu từ node đầu tiên

        # Kiểm tra xem fast_pointer có node kế tiếp hay không
        # Kiểm tra node kế tiếp có node nữa không -> Nếu cả 2 NULL thì dừng
        while fast_pointer.next_node and fast_pointer.next_node.next_node:
            fast_pointer = (
                fast_pointer.next_node.next_node
            )  # Gán fast_pointer nhảy 2 node // Mục đích: tăng tốc độ di chuyển gấp đôi so với slow_pointer
            slow_pointer = (
                slow_pointer.next_node
            )  # Gán slow_pointer nhảy 1 node // Tốc độ di chuyển chậm hơn nên sẽ dừng ở giữa danh sách

        return slow_pointer  # Khi thoát vòng lặp thì trả về slow_pointer // Lúc này slow_pointer chính là node middle

    def insert(self, data):
        self.size = self.size + 1  # Tăng size lên 1
        new_node = Node(data)  # Tạo node mới

        if not self.head:  # Kiểm tra nếu head None thì gán bằng node mới
            self.head = new_node
        else:  # Ngược lại, gán next của node mới = head cũ
            new_node.next_node = self.head
            self.head = new_node  # Gán node mới thành head

    def traverse_list(self):
        actual_node = self.head  # Bắt đầu duyệt từ node đầu tiên (head)

        while actual_node is not None:  # Nếu còn node tiếp theo thì duyệt
            print(
                "%d" % actual_node.data
            )  # In ra màn hình giá trị data của node hiện tại
            actual_node = actual_node.next_node  # Chuyển sang node tiếp theo để duyệt


if __name__ == "__main__":
    linked_list = LinkedList()  # Khởi tạo LinkedList

    linked_list.insert(28)
    linked_list.insert(10)
    linked_list.insert(2003)

    print(linked_list.get_middle_node().data)
