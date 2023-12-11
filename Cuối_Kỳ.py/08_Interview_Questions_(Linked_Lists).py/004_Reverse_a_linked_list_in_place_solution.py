class Node:  # Khai báo class Node
    def __init__(self, data):  # Hàm khởi tạo Node, có tham số là data
        self.data = data  # Gán giá trị data vào thuộc tính self.data của Node
        self.next_node = None


class LinkedList(object):  # Khai báo Class LinkedList
    def __init__(self):  # Khởi tạo hàm
        self.head = None  # Khởi tạo thuộc tính self.head và gán ban đầu = None
        self.size = 0

    def reverse(self):
        current_node = (
            self.head
        )  # Khai báo biến current_node, gán bằng self.head (bắt đầu node đầu tiên)
        previous_node = None  # Khai báo biến previous_node, gán ban đầu = None
        next_node = None  # Khai báo biến next_node, ban đầu = None

        while current_node is not None:  # Vòng lặp while duyệt từ đầu đến cuối
            next_node = (
                current_node.next_node
            )  # Lưu next_node hiện tại vào biến next_node
            current_node.next_node = previous_node  # Đảo chiều next_node của node hiện tại sang previous_node
            previous_node = current_node  # Cập nhật previous_node = node hiện tại
            current_node = next_node  # Chuyển sang node kế tiếp

        self.head = previous_node  # Sau vòng lặp, gán lại head = previous_node

    def insert_start(self, data):
        self.size = self.size + 1  # Tăng biến đếm size lên 1
        new_node = Node(data)  # Tạo node mới

        if not self.head:  #  Nếu danh sách rỗng
            self.head = new_node  # Thì gán node mới là head
        else:  # Nếu danh sách có node, nối node mới vào trước head
            new_node.next_node = self.head
            self.head = new_node

    def remove(self, data):
        if self.head is None:  # Kiểm tra danh sách có rỗng không
            return  # Nếu rỗng thì dừng lại luôn

        self.size = self.size - 1  # Giảm biến đếm size xuống 1

        current_node = self.head  # Gán current_node = self.head để bắt đầu duyệt từ đầu
        previous_node = None  # Khởi tạo previous_node = None

        while current_node.data != data:  # Sử dụng vòng lặp while để duyệt danh sách
            previous_node = current_node  # Cập nhật previous_node
            current_node = (
                current_node.nextNode
            )  # Chuyển current_node sang node tiếp theo

        if previous_node is None:  # Nếu node cần xóa là node đầu tiên
            self.head = current_node.nextNode  # Gán lại head bằng node kế tiếp
        else:
            previous_node.nextNode = (
                current_node.nextNode
            )  # gán nextNode của previous_node bỏ qua node cần xóa

    def size1(self):  # Khai báo phương thức size1()
        return self.size  # Trả về giá trị của biến đếm size

    def size2(
        self,
    ):  # Khai báo phương thức size2(). Dùng để đếm kích thước linked list bằng cách duyệt qua các node
        actual_node = (
            self.head
        )  # Khởi tạo biến actual_node = self.head (bắt đầu node đầu tiên)
        size = 0  # Khởi tạo biến size = 0 (đếm số node)

        while actual_node is not None:  # Sử dụng vòng lặp while để duyệt danh sách
            size += 1  # Tăng biến size lên 1 mỗi lần gặp 1 node
            actual_node = actual_node.next_node  # Chuyển actual_node sang node kế tiếp

        return size  # Sau khi duyệt xong, trả về biến size -> số node

    def insert_end(self, data):
        self.size = self.size + 1  # Tăng size lên 1
        new_node = Node(data)  # Tạo node cần chèn
        actual_node = self.head  # Gán actual_node = self.head

        while actual_node.next_node is not None:  # Duyệt tới khi gặp node cuối cùng
            actual_node = actual_node.next_node

        actual_node.next_node = new_node  # Gán node cuối cùng trỏ tới node mới

    def traverse_list(
        self,
    ):  # Khai báo phương thức traverse_list() để duyệt và in các node trong danh sách liên kết
        actual_node = (
            self.head
        )  # Khai báo biến actual_node, gán bằng self.head (bắt đầu từ node đầu tiên của danh sách)

        while actual_node is not None:  # Sử dụng vòng lặp while để duyệt các node
            print(
                "%d" % actual_node.data
            )  # In ra màn hình data của node hiện tại và hiển thị dữ liệu cho người dùng
            actual_node = (
                actual_node.next_node
            )  # Gán actual_node = node liền kề phía sau, chuyển sang node tiếp theo để duyệt


if __name__ == "__main__":
    linked_list = LinkedList()

    linked_list.insert_start(2)  # Thêm lần lượt các phần tử vào đầu danh sách
    linked_list.insert_start(8)
    linked_list.insert_start(28)
    linked_list.insert_start(10)
    linked_list.insert_start(2003)
    linked_list.traverse_list()  # In ra danh sách ban đầu
    linked_list.reverse()  # Gọi phương thức reverse() để đảo ngược danh sách
    print("Reversed list")  # In ra "Reversed list" và danh sách sau khi đã đảo ngược
    linked_list.traverse_list()
