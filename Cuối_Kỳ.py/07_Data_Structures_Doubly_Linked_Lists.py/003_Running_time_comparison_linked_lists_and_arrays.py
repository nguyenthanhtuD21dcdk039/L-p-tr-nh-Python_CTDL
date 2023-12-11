import time  # Import thư viện time để sử dụng các hàm liên quan tới thời gian


class Node:  # Khai báo class Node
    def __init__(self, data):  # Hàm khởi tạo Node, có tham số là data
        self.data = data  # Gán giá trị data vào thuộc tính self.data của Node
        self.next_node = None


class LinkedList:  # Khai báo Class LinkedList
    def __init__(self):  # Khởi tạo hàm
        self.head = None  # Khởi tạo thuộc tính self.head và gán ban đầu = None
        self.size = 0

    def insert(self, data):
        self.size = self.size + 1  # Tăng size lên 1
        new_node = Node(data)  # Tạo node mới

        if not self.head:  # Kiểm tra nếu head None thì gán bằng node mới
            self.head = new_node
        else:  # Ngược lại, gán next của node mới = head cũ
            new_node.next_node = self.head
            self.head = new_node  # Gán node mới thành head


if __name__ == "__main__":
    linked_list = LinkedList()  # Khởi tạo LinkedList
    now = time.time()  # Lấy thời gian bắt đầu

    for i in range(500000):
        linked_list.insert(i)

    print(
        "Inserting items into Linked List in %ss" % str(time.time() - now)
    )  # In ra thời gian thực thi

    array = []
    now = time.time()

    for i in range(500000):
        array.insert(0, i)  # Thực hiện insert vào array

    print(
        "Inserting items into Array in %ss" % str(time.time() - now)
    )  # In ra thời gian thực thi array
