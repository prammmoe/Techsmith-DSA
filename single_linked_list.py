# Inisialisasi Class Node 
class Node: 
    def __init__(self, data):
        self.data = data # Data yang disimpan di dalam node
        self.next = None # Pointer ke node selanjutnya

        # | head | pointer | -> | data | pointer | dst

class SingleLinkedList:
    def __init__(self):
        self.head = None # Pointer ke node pertama
        self.size = 0 # Ukuran linked list

    def is_empty(self):
        """
        Fungsi untuk memeriksa apakah linked list kosong
        """
        return self.head is None
    
    def get_size(self):
        """
        Fungsi untuk mendapatkan ukuran linked list
        """
        return self.size
    
    def add_first(self, data):
        """
        Fungsi untuk menambahkan node di awal linked list
        """
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.size += 1

    def add_last(self, data):
        """
        Fungsi untuk menambahkan node baru di akhir linked list
        """
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
        else:
            current = self.head
            # Traversal hingga akhir linked list
            while current.next:
                current = current.next
            current.next = new_node
        self.size += 1

    # Add at position?

    def remove_first(self):
        """
        Fungsi untuk menghapus node pertama dari linked list
        """
        if self.is_empty():
            raise Exception("Linked list kosong")
        
        removed_data = self.head.data
        self.head = self.head.next
        self.size -= 1
        return removed_data
    
    def remove_last(self):
        """
        Fungsi untuk menghapus node terakhir dari linked list
        """
        if self.is_empty():
            raise Exception("Linked list kosong")
        
        # Cek apakah hanya ada satu elemen aja
        if self.head.next is None:
            removed_data = self.head.data
            self.head = None
            self.size -= 1
            return removed_data
        
        # Variabel untuk pengecekan elemen secara traversal
        current = self.head 
        # Traversal LL dengan minimal ada dua node lagi setelah node saat ini
        while current.next.next:
            current = current.next

        removed_data = current.next.data
        current.next = None
        self.size -= 1
        return removed_data
    
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
    
    def display(self):
        """
        Menampilkan seluruh elemen linked list
        """
        elements = []
        current = self.head
        
        while current:
            elements.append(str(current.data))
            current = current.next
        
        return " -> ".join(elements)
    
    def clear(self):
        """
        Mengosongkan linked list
        """
        self.head = None
        self.size = 0

# Impl
if __name__ == "__main__":
    sll = SingleLinkedList()

    print("\nMenambahkan elemen")
    sll.add_first(10)
    sll.add_first(200)
    sll.add_last(2000)
    sll.add_last(4000)
    print("Linked List:", sll.display())
    print("Ukuran", sll.get_size())

    print("\nMengurangi elemen")
    sll.remove_last()
    print("Linked List:", sll.display())
    print("Ukuran", sll.get_size())
