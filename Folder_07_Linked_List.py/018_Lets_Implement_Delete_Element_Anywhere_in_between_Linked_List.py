class _Node:
    """Định nghĩa một lớp _Node để tạo Node trong danh sách liên kết."""

    __slots__ = (
        "_element",
        "_next",
    )  # Sử dụng __slots__ để tối ưu hóa việc quản lý bộ nhớ

    def __init__(self, element, next):
        """Phương thức khởi tạo của lớp _Node với tham số element và next."""
        self._element = (
            element  # Gán giá trị của tham số element cho thuộc tính _element
        )
        self._next = next  # Gán giá trị của tham số next cho thuộc tính _next


class LinkedList:
    """Định nghĩa một lớp LinkedList để tạo danh sách liên kết."""

    def __init__(self):
        """Phương thức khởi tạo của lớp LinkedList."""
        self._head = None  # Gán giá trị đầu của danh sách liên kết là None
        self._tail = None  # Gán giá trị đuôi của danh sách liên kết là None
        self._size = 0  # Khởi tạo biến _size để đếm số phần tử trong danh sách liên kết

    def __len__(self):
        """Phương thức để lấy độ dài của danh sách liên kết."""
        return self._size  # Trả về giá trị của biến _size

    def isempty(self):
        """Phương thức để kiểm tra xem danh sách liên kết có rỗng không."""
        return self._size == 0  # Trả về True nếu danh sách rỗng, ngược lại là False

    def addlast(self, e):
        """Phương thức để thêm một phần tử e vào cuối danh sách liên kết."""
        newest = _Node(e, None)  # Tạo một Node mới có giá trị là e và next trỏ đến None
        if self.isempty():
            self._head = newest  # Nếu rỗng, gán phần đầu danh sách là newest
        else:
            self._tail._next = newest  # Nếu không rỗng, cập nhật con trỏ next của Node cuối cùng đến newest
        self._tail = newest  # Cập nhật Node cuối danh sách là newest
        self._size += (
            1  # Tăng giá trị của _size lên 1 để đếm số phần tử trong danh sách
        )

    def addfirst(self, e):
        """Phương thức để thêm một phần tử e vào đầu danh sách liên kết."""
        newest = _Node(
            e, None
        )  # Tạo một Node mới `newest` với giá trị `e` và con trỏ `next` trỏ đến `None`.
        if self.isempty():  # Kiểm tra xem danh sách liên kết có rỗng không.
            self._head = (
                newest  # Nếu rỗng, gán phần tử đầu của danh sách liên kết là `newest`.
            )
            self._tail = newest  # Vì danh sách rỗng, nên phần tử cuối cũng là `newest`.
        else:
            newest._next = (
                self._head
            )  # Cập nhật con trỏ `next` của `newest` để trỏ đến phần tử đầu tiên của danh sách liên kết hiện tại. Điều này làm cho `newest` trở thành phần tử đầu tiên của danh sách.
            self._head = newest  # Cập nhật con trỏ `head` để trỏ đến `newest`, làm cho `newest` trở thành phần tử đầu tiên của danh sách.
        self._size += 1  # Tăng kích thước của danh sách liên kết lên 1 (nếu bạn đang theo dõi kích thước).

    def addany(self, e, position):
        """Phương thức để thêm một phần tử e vào vị trí position trong danh sách liên kết."""
        newest = _Node(e, None)  # Tạo một Node mới có giá trị là e và next trỏ đến None
        p = self._head  # Gán p là phần tử đầu tiên của danh sách liên kết
        i = 1  # Gán i = 1
        while (
            i < position - 1
        ):  # Kiểm tra vị trí của i có phải là vị trí cần chèn vào chưa
            p = p._next  # Trỏ tới phần tử kế tiếp trong danh sách liên kết
            i = i + 1  # Tăng biến đếm i
        newest._next = (
            p._next
        )  # Trỏ giá trị của biến cần chèn vào đến phần tử danh sách liên kết kế tiếp
        p._next = newest  # Trỏ giá trị tiếp theo của p là biến cần chèn vào
        self._size += 1  # Tăng kích thước của danh sách liên kết

    def removefirst(self):  # tạo hàm xóa phần tử đầu tiên của danh sách liên kết
        if self.isempty():  # kiểm tra nếu danh sách trống
            print("List is empty")  # nếu danh sách trống thì in ra list trống
            return
        e = (
            self._head._element
        )  # gán e là giá trị của phần tử đầu tiên danh sách liên kết
        self._head = (
            self._head._next
        )  # chúng ta sẽ trỏ head đến phần tử thứ 2, coi như phần tử thứ 2 là phần tử đầu, bỏ qua phần tử đầu tiên
        self._size -= 1  # sau khi xóa thì giảm kích thước danh sách liên kết đi 1
        if self.isempty():  # kiểm tra lại nếu sau khi xóa danh sách liên kết trống
            self._tail = None  # nếu linkedlist trống thì gán phần tử cuối cùng là None
        return e  # trả về giá trị e để in ra giá trị của phần tử đã xóa nêu cần

    def removelast(self):  # Hàm xóa phần tử cuối cùng của danh sách liên kết
        if self.isempty():  # Kiểm tra xem danh sách có rỗng không
            print("List is empty")  # In ra thông báo nếu danh sách rỗng
            return

        p = self._head  # Gán p là phần tử đầu tiên của danh sách liên kết
        i = 1  # Khởi tạo biến đếm i

        while i < len(self) - 1:  # Duyệt đến phần tử kế cuối
            p = p._next  # Di chuyển con trỏ p đến phần tử kế tiếp
            i = i + 1  # Tăng biến đếm i

        self._tail = p  # Cập nhật con trỏ `_tail` để trỏ đến phần tử kế cuối (hiện tại)
        p = p._next  # Di chuyển con trỏ p đến phần tử bị xóa để lấy giá trị của nó
        e = p._element  # Lưu trữ giá trị của phần tử bị xóa trong biến e

        self._tail._next = None  # Trỏ con trỏ `_next` của phần tử cuối cùng hiện tại thành None, đánh dấu phần tử cuối cùng của danh sách

        self._size -= 1  # Giảm kích thước của danh sách liên kết đi 1
        return e  # Trả về giá trị của phần tử bị xóa

    # Bắt đầu 018
    def removeany(self, position):  # Tạo hàm xóa tại vị trí position
        p = self._head  # p là phần tử đầu tiên
        i = 1  # Khởi tạo biến đếm i

        while (
            i < position - 1
        ):  # Vòng lặp chạy kiểm tra đến vị trí trước giá trị cần xóa
            p = p._next  # Trỏ đến phần tử kế tiếp
            i = i + 1  # Tăng giá trị của i

        e = p._next._element  # Biến e gán bằng giá trị của phần tử cần xóa
        p._next = (
            p._next._next
        )  # Trỏ giá trị tới nút hiện tại không trỏ tới giá trị cần xóa nữa mà trỏ tới phần tử tiếp theo của phần tử cần xóa
        self._size -= 1  # Giảm kích thước danh sách liên kết
        return e  # Trả về giá trị cần xóa

    # Kết thúc 018

    def search(self, key):
        """Phương thức để tìm kiếm giá trị key trong danh sách liên kết đơn."""
        p = self._head  # Gán giá trị đầu là p
        index = 0  # Biến index để lưu số thứ tự của phần tử cần tìm
        while p:  # Tạo vòng lặp while
            if p._element == key:  # Nếu giá trị của phần tử hiện tại bằng key cần tìm
                return index  # Trả về giá trị index
            p = p._next  # Duyệt tới phần tử kế tiếp
            index += 1  # Tăng giá trị của index
        return -1  # Nếu không tìm thấy, trả về -1

    def display(self):
        """Phương thức để hiển thị các phần tử trong danh sách liên kết."""
        p = self._head  # Gán p là giá trị đầu của danh sách liên kết
        while p:  # Sử dụng vòng lặp while để duyệt qua danh sách
            print(
                p._element, end=" --> "
            )  # In ra giá trị của Node hiện tại, end=' --> ' để tạo dấu nối
            p = p._next  # Di chuyển con trỏ p đến phần tử tiếp theo trong danh sách
        print()  # In một dòng mới để kết thúc danh sách


L = LinkedList()
L.addlast(2)
L.addlast(8)
L.addlast(28)
L.addlast(10)
L.addlast(2003)
L.display()
print("Size:", len(L))
eleany = L.removeany(
    3
)  # Gọi phương thức removeany để xóa phần tử ở vị trí 3 và lưu giá trị vào biến 'eleany'
L.display()  # Hiển thị danh sách liên kết sau khi xóa phần tử
print(
    "element remove ", eleany
)  # In ra giá trị của phần tử đã bị xóa từ danh sách liên kết