class Node:
    """
    Kelas Node untuk Doubly Linked List
    """
    def __init__(self, data):
        self.data = data    # Data yang disimpan dalam node
        self.next = None    # Pointer ke node selanjutnya
        self.prev = None    # Pointer ke node sebelumnya
        
class DoublyLinkedList:
    """
    Implementasi Doubly Linked List
    """
    def __init__(self):
        self.head = None    # Pointer ke node pertama
        self.tail = None    # Pointer ke node terakhir
        self.size = 0       # Ukuran linked list
    
    def is_empty(self):
        """
        Memeriksa apakah linked list kosong
        """
        return self.head is None
    
    def get_size(self):
        """
        Mendapatkan ukuran linked list
        """
        return self.size
    
    def add_first(self, data):
        """
        Menambahkan node baru di awal linked list
        """
        new_node = Node(data)
        
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        
        self.size += 1
    
    def add_last(self, data):
        """
        Menambahkan node baru di akhir linked list
        """
        new_node = Node(data)
        
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        
        self.size += 1
    
    def add_at(self, data, position):
        """
        Menambahkan node baru pada posisi tertentu
        """
        if position < 0 or position > self.size:
            raise IndexError("Posisi tidak valid")
        
        if position == 0:
            self.add_first(data)
            return
        
        if position == self.size:
            self.add_last(data)
            return
        
        new_node = Node(data)
        
        if position <= self.size // 2:
            # Traversal dari depan jika posisi di paruh pertama
            current = self.head
            for _ in range(position):
                current = current.next
            
            new_node.prev = current.prev
            new_node.next = current
            current.prev.next = new_node
            current.prev = new_node
        else:
            # Traversal dari belakang jika posisi di paruh kedua
            current = self.tail
            for _ in range(self.size - position - 1):
                current = current.prev
            
            new_node.next = current.next
            new_node.prev = current
            current.next.prev = new_node
            current.next = new_node
        
        self.size += 1
    
    def remove_first(self):
        """
        Menghapus node pertama dari linked list
        """
        if self.is_empty():
            raise Exception("Linked list kosong")
        
        removed_data = self.head.data
        
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
        
        self.size -= 1
        return removed_data
    
    def remove_last(self):
        """
        Menghapus node terakhir dari linked list
        """
        if self.is_empty():
            raise Exception("Linked list kosong")
        
        removed_data = self.tail.data
        
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        
        self.size -= 1
        return removed_data
    
    def remove_at(self, position):
        """
        Menghapus node pada posisi tertentu
        """
        if self.is_empty():
            raise Exception("Linked list kosong")
        
        if position < 0 or position >= self.size:
            raise IndexError("Posisi tidak valid")
        
        if position == 0:
            return self.remove_first()
        
        if position == self.size - 1:
            return self.remove_last()
        
        if position <= self.size // 2:
            # Traversal dari depan jika posisi di paruh pertama
            current = self.head
            for _ in range(position):
                current = current.next
        else:
            # Traversal dari belakang jika posisi di paruh kedua
            current = self.tail
            for _ in range(self.size - position - 1):
                current = current.prev
        
        current.prev.next = current.next
        current.next.prev = current.prev
        
        removed_data = current.data
        self.size -= 1
        
        return removed_data
    
    def get(self, position):
        """
        Mendapatkan data pada posisi tertentu
        """
        if self.is_empty():
            raise Exception("Linked list kosong")
        
        if position < 0 or position >= self.size:
            raise IndexError("Posisi tidak valid")
        
        if position <= self.size // 2:
            # Traversal dari depan jika posisi di paruh pertama
            current = self.head
            for _ in range(position):
                current = current.next
        else:
            # Traversal dari belakang jika posisi di paruh kedua
            current = self.tail
            for _ in range(self.size - position - 1):
                current = current.prev
        
        return current.data
    
    def search(self, data):
        """
        Mencari posisi data dalam linked list
        """
        if self.is_empty():
            return -1
        
        current = self.head
        position = 0
        
        while current:
            if current.data == data:
                return position
            current = current.next
            position += 1
        
        return -1  # Data tidak ditemukan
    
    def update(self, data, position):
        """
        Memperbarui data pada posisi tertentu
        """
        if self.is_empty():
            raise Exception("Linked list kosong")
        
        if position < 0 or position >= self.size:
            raise IndexError("Posisi tidak valid")
        
        if position <= self.size // 2:
            # Traversal dari depan jika posisi di paruh pertama
            current = self.head
            for _ in range(position):
                current = current.next
        else:
            # Traversal dari belakang jika posisi di paruh kedua
            current = self.tail
            for _ in range(self.size - position - 1):
                current = current.prev
        
        current.data = data
    
    def display_forward(self):
        """
        Menampilkan seluruh elemen linked list dari depan ke belakang
        """
        elements = []
        current = self.head
        
        while current:
            elements.append(str(current.data))
            current = current.next
        
        return " <-> ".join(elements)
    
    def display_backward(self):
        """
        Menampilkan seluruh elemen linked list dari belakang ke depan
        """
        elements = []
        current = self.tail
        
        while current:
            elements.append(str(current.data))
            current = current.prev
        
        return " <-> ".join(elements)
    
    def clear(self):
        """
        Mengosongkan linked list
        """
        self.head = None
        self.tail = None
        self.size = 0


# Contoh penggunaan
if __name__ == "__main__":
    dll = DoublyLinkedList()
    
    print("Menambahkan elemen di awal dan akhir")
    dll.add_first(10)
    dll.add_last(20)
    dll.add_first(5)
    dll.add_last(30)
    print("Linked List (Maju):", dll.display_forward())
    print("Linked List (Mundur):", dll.display_backward())
    print("Ukuran:", dll.get_size())
    
    print("\nMenambahkan elemen pada posisi tertentu")
    dll.add_at(15, 2)
    print("Linked List (Maju):", dll.display_forward())
    
    print("\nMendapatkan elemen pada posisi 2:", dll.get(2))
    
    print("\nMencari posisi elemen 20:", dll.search(20))
    print("Mencari posisi elemen 100:", dll.search(100))
    
    print("\nMemperbarui elemen pada posisi 1 menjadi 12")
    dll.update(12, 1)
    print("Linked List (Maju):", dll.display_forward())
    
    print("\nMenghapus elemen pertama:", dll.remove_first())
    print("Linked List (Maju):", dll.display_forward())
    
    print("\nMenghapus elemen terakhir:", dll.remove_last())
    print("Linked List (Maju):", dll.display_forward())
    
    print("\nMenghapus elemen pada posisi 1:", dll.remove_at(1))
    print("Linked List (Maju):", dll.display_forward())
    
    print("\nMengosongkan linked list")
    dll.clear()
    print("Apakah linked list kosong?", dll.is_empty())