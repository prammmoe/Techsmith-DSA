class Queue:
    """
    Implementasi Queue (Antrian) menggunakan list Python
    
    Queue mengikuti prinsip FIFO (First-In-First-Out):
    Elemen pertama yang masuk adalah elemen pertama yang keluar
    """
    def __init__(self):
        """
        Inisialisasi queue kosong
        """
        self.items = []
        
    def is_empty(self):
        """
        Memeriksa apakah queue kosong
        
        Returns:
            bool: True jika queue kosong, False jika tidak
        """
        return len(self.items) == 0
        
    def enqueue(self, item):
        """
        Menambahkan item ke dalam queue (di bagian belakang)
        
        Args:
            item: Elemen yang akan ditambahkan ke queue
        """
        self.items.append(item) 
        
    def dequeue(self):
        """
        Mengeluarkan item dari queue (dari bagian depan)
        
        Returns:
            item: Elemen yang dikeluarkan dari bagian depan queue
            
        Raises:
            IndexError: Jika queue kosong
        """
        if self.is_empty():
            raise IndexError("Dequeue dari queue kosong")
        return self.items.pop(0) # Indeks dimulai dari 0, jadi 0 yang paling depan
        
    def peek(self):
        """
        Melihat item di bagian depan queue tanpa mengeluarkannya
        
        Returns:
            item: Elemen di bagian depan queue
            
        Raises:
            IndexError: Jika queue kosong
        """
        if self.is_empty():
            raise IndexError("Peek dari queue kosong")
        return self.items[0] # Ini kita ngambil indeks paling depan
        
    def size(self):
        """
        Mendapatkan jumlah item dalam queue
        
        Returns:
            int: Jumlah item dalam queue
        """
        return len(self.items)
    
    def clear(self):
        """
        Mengosongkan queue
        """
        self.items = []
        
    def __str__(self):
        """
        Mengembalikan representasi string dari queue
        
        Returns:
            str: Representasi string dari queue
        """
        return str(self.items)


# class QueueLinkedList:
#     """
#     Implementasi Queue (Antrian) menggunakan Linked List
    
#     Queue mengikuti prinsip FIFO (First-In-First-Out):
#     Elemen pertama yang masuk adalah elemen pertama yang keluar
    
#     Implementasi ini lebih efisien untuk operasi dequeue karena
#     kompleksitas waktunya O(1), bukan O(n) seperti pada implementasi list
#     """
#     class Node:
#         """
#         Kelas Node untuk QueueLinkedList
#         """
#         def __init__(self, data):
#             self.data = data
#             self.next = None
    
#     def __init__(self):
#         """
#         Inisialisasi queue kosong
#         """
#         self.front = None  # Pointer ke elemen depan (untuk dequeue)
#         self.rear = None   # Pointer ke elemen belakang (untuk enqueue)
#         self.size = 0      # Ukuran queue
    
#     def is_empty(self):
#         """
#         Memeriksa apakah queue kosong
        
#         Returns:
#             bool: True jika queue kosong, False jika tidak
#         """
#         return self.front is None
    
#     def enqueue(self, item):
#         """
#         Menambahkan item ke dalam queue (di bagian belakang)
        
#         Args:
#             item: Elemen yang akan ditambahkan ke queue
#         """
#         new_node = self.Node(item)
        
#         if self.is_empty():
#             self.front = new_node
#         else:
#             self.rear.next = new_node
            
#         self.rear = new_node
#         self.size += 1
    
#     def dequeue(self):
#         """
#         Mengeluarkan item dari queue (dari bagian depan)
        
#         Returns:
#             item: Elemen yang dikeluarkan dari bagian depan queue
            
#         Raises:
#             IndexError: Jika queue kosong
#         """
#         if self.is_empty():
#             raise IndexError("Dequeue dari queue kosong")
            
#         removed_item = self.front.data
#         self.front = self.front.next
        
#         # Jika queue menjadi kosong setelah dequeue
#         if self.front is None:
#             self.rear = None
            
#         self.size -= 1
#         return removed_item
    
#     def peek(self):
#         """
#         Melihat item di bagian depan queue tanpa mengeluarkannya
        
#         Returns:
#             item: Elemen di bagian depan queue
            
#         Raises:
#             IndexError: Jika queue kosong
#         """
#         if self.is_empty():
#             raise IndexError("Peek dari queue kosong")
            
#         return self.front.data
    
#     def get_size(self):
#         """
#         Mendapatkan jumlah item dalam queue
        
#         Returns:
#             int: Jumlah item dalam queue
#         """
#         return self.size
    
#     def clear(self):
#         """
#         Mengosongkan queue
#         """
#         self.front = None
#         self.rear = None
#         self.size = 0
    
#     def __str__(self):
#         """
#         Mengembalikan representasi string dari queue
        
#         Returns:
#             str: Representasi string dari queue
#         """
#         if self.is_empty():
#             return "[]"
            
#         items = []
#         current = self.front
        
#         while current:
#             items.append(str(current.data))
#             current = current.next
            
#         return f"[{', '.join(items)}]"


# Contoh penggunaan Queue dengan list
def test_queue_list():
    q = Queue()
    
    print("Apakah queue kosong?", q.is_empty())  # True
    
    print("\nMenambahkan elemen ke queue:")
    q.enqueue(10)
    print("Queue setelah enqueue(10):", q)
    
    q.enqueue(20)
    print("Queue setelah enqueue(20):", q)
    
    q.enqueue(30)
    print("Queue setelah enqueue(30):", q)
    
    print("\nUkuran queue:", q.size())  # 3
    
    print("\nMelihat elemen depan queue:", q.peek())  # 10
    
    print("\nMengeluarkan elemen dari queue:")
    print("Dequeue:", q.dequeue())  # 10
    print("Queue setelah dequeue:", q)
    
    print("Dequeue:", q.dequeue())  # 20
    print("Queue setelah dequeue:", q)
    
    print("\nUkuran queue sekarang:", q.size())  # 1
    
    print("\nMengosongkan queue")
    q.clear()
    print("Apakah queue kosong?", q.is_empty())  # True


# # Contoh penggunaan Queue dengan Linked List
# def test_queue_linked_list():
#     q = QueueLinkedList()
    
#     print("Apakah queue kosong?", q.is_empty())  # True
    
#     print("\nMenambahkan elemen ke queue:")
#     q.enqueue(10)
#     print("Queue setelah enqueue(10):", q)
    
#     q.enqueue(20)
#     print("Queue setelah enqueue(20):", q)
    
#     q.enqueue(30)
#     print("Queue setelah enqueue(30):", q)
    
#     print("\nUkuran queue:", q.get_size())  # 3
    
#     print("\nMelihat elemen depan queue:", q.peek())  # 10
    
#     print("\nMengeluarkan elemen dari queue:")
#     print("Dequeue:", q.dequeue())  # 10
#     print("Queue setelah dequeue:", q)
    
#     print("Dequeue:", q.dequeue())  # 20
#     print("Queue setelah dequeue:", q)
    
#     print("\nUkuran queue sekarang:", q.get_size())  # 1
    
#     print("\nMengosongkan queue")
#     q.clear()
#     print("Apakah queue kosong?", q.is_empty())  # True


# Menjalankan pengujian
if __name__ == "__main__":
    test_queue_list()