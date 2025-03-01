class Node:
    def __init__(self, data):
        self.data = data  # Data yang disimpan dalam node
        self.next = None  # Pointer ke node selanjutnya
        
class CircularLinkedList:
    def __init__(self):
        self.head = None  # Pointer ke node pertama
        self.tail = None  # Pointer ke node terakhir
        self.size = 0     # Ukuran linked list
    
    def is_empty(self):
        return self.head is None
    
    def get_size(self):
        return self.size
    
    def add_first(self, data):
        new_node = Node(data)
        
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node  # Referensi ke diri sendiri untuk membentuk lingkaran
        else:
            new_node.next = self.head
            self.head = new_node
            self.tail.next = self.head  # Tail selalu menunjuk ke head untuk membentuk lingkaran
        
        self.size += 1
    
    def add_last(self, data):
        new_node = Node(data)
        
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node 
        else:
            new_node.next = self.head
            self.tail.next = new_node
            self.tail = new_node
        
        self.size += 1
    
    def add_at(self, data, position):
        if position < 0 or position > self.size:
            raise IndexError("Posisi tidak valid")
        
        if position == 0:
            self.add_first(data)
            return
        
        if position == self.size:
            self.add_last(data)
            return
        
        new_node = Node(data)
        current = self.head
        
        # Traversal hingga posisi yang ditentukan
        for _ in range(position - 1):
            current = current.next
        
        new_node.next = current.next
        current.next = new_node
        
        self.size += 1
    
    def remove_first(self):
        if self.is_empty():
            raise Exception("Linked list kosong")
        
        removed_data = self.head.data
        
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.tail.next = self.head
        
        self.size -= 1
        return removed_data
    
    def remove_last(self):
        if self.is_empty():
            raise Exception("Linked list kosong")
        
        removed_data = self.tail.data
        
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            current = self.head
            
            # Traversal hingga node sebelum tail
            while current.next != self.tail:
                current = current.next
            
            current.next = self.head
            self.tail = current
        
        self.size -= 1
        return removed_data
    
    def remove_at(self, position):
        if self.is_empty():
            raise Exception("Linked list kosong")
        
        if position < 0 or position >= self.size:
            raise IndexError("Posisi tidak valid")
        
        if position == 0:
            return self.remove_first()
        
        if position == self.size - 1:
            return self.remove_last()
        
        current = self.head
        
        # Traversal hingga node sebelum yang akan dihapus
        for _ in range(position - 1):
            current = current.next
        
        removed_data = current.next.data
        current.next = current.next.next
        
        self.size -= 1
        return removed_data
    
    def get(self, position):
        """
        Get data at some position
        """
        if self.is_empty():
            raise Exception("Linked list kosong")
        
        if position < 0 or position >= self.size:
            raise IndexError("Posisi tidak valid")
        
        current = self.head
        
        # Traversal hingga posisi yang ditentukan
        for _ in range(position):
            current = current.next
        
        return current.data
    
    def search(self, data):
        if self.is_empty():
            return -1
        
        current = self.head
        position = 0
        
        # Traversal satu putaran penuh
        while True:
            if current.data == data:
                return position
            
            current = current.next
            position += 1
            
            # Jika sudah kembali ke head, berarti data tidak ditemukan
            if current == self.head or position >= self.size:
                break
        
        return -1  # Data tidak ditemukan
    
    def update(self, data, position):
        """
        Memperbarui data pada posisi tertentu
        """
        if self.is_empty():
            raise Exception("Linked list kosong")
        
        if position < 0 or position >= self.size:
            raise IndexError("Posisi tidak valid")
        
        current = self.head
        
        # Traversal hingga posisi yang ditentukan
        for _ in range(position):
            current = current.next
        
        current.data = data
    
    def display(self):
        """
        Menampilkan seluruh elemen linked list
        """
        if self.is_empty():
            return "Linked list kosong"
        
        elements = []
        current = self.head
        
        # Traversal satu putaran penuh
        while True:
            elements.append(str(current.data))
            current = current.next
            
            if current == self.head:
                break
        
        return " -> ".join(elements) + " -> (kembali ke " + str(self.head.data) + ")"
    
    def clear(self):
        self.head = None
        self.tail = None
        self.size = 0


if __name__ == "__main__":
    cll = CircularLinkedList()
    
    print("Menambahkan elemen di awal dan akhir")
    cll.add_first(10)
    cll.add_last(20)
    cll.add_first(5)
    cll.add_last(30)
    print("Linked List:", cll.display())
    print("Ukuran:", cll.get_size())
    
    print("\nMenambahkan elemen pada posisi tertentu")
    cll.add_at(15, 2)
    print("Linked List:", cll.display())
    
    print("\nMendapatkan elemen pada posisi 2:", cll.get(2))
    
    print("\nMencari posisi elemen 20:", cll.search(20))
    print("Mencari posisi elemen 100:", cll.search(100))
    
    print("\nMemperbarui elemen pada posisi 1 menjadi 12")
    cll.update(12, 1)
    print("Linked List:", cll.display())
    
    print("\nMenghapus elemen pertama:", cll.remove_first())
    print("Linked List:", cll.display())
    
    print("\nMenghapus elemen terakhir:", cll.remove_last())
    print("Linked List:", cll.display())
    
    print("\nMenghapus elemen pada posisi 1:", cll.remove_at(1))
    print("Linked List:", cll.display())
    
    print("\nMengosongkan linked list")
    cll.clear()
    print("Apakah linked list kosong?", cll.is_empty())