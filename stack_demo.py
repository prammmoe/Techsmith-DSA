class Stack:
    """
    Implementasi Stack (Tumpukan) menggunakan list Python
    
    Stack mengikuti prinsip LIFO (Last-In-First-Out):
    Elemen terakhir yang masuk adalah elemen pertama yang keluar
    """
    def __init__(self):
        """
        Inisialisasi stack kosong
        """
        self.items = []
        
    def is_empty(self):
        """
        Memeriksa apakah stack kosong
        
        Returns:
            bool: True jika stack kosong, False jika tidak
        """
        return len(self.items) == 0 # return boolean
        
    def push(self, item):
        """
        Menambahkan item ke dalam stack (di bagian atas)
        
        Args:
            item: Elemen yang akan ditambahkan ke stack
        """
        self.items.append(item)
        
    def pop(self):
        """
        Mengeluarkan item dari stack (dari bagian atas)
        
        Returns:
            item: Elemen yang dikeluarkan dari bagian atas stack
            
        Raises:
            IndexError: Jika stack kosong
        """
        if self.is_empty():
            raise IndexError("Pop dari stack kosong")
        return self.items.pop() # Di Python sendiri, defaultnya adalah last item
        
    def peek(self):
        """
        Melihat item di bagian atas stack tanpa mengeluarkannya
        
        Returns:
            item: Elemen di bagian atas stack
            
        Raises:
            IndexError: Jika stack kosong
        """
        if self.is_empty():
            raise IndexError("Peek dari stack kosong")
        return self.items[-1] # -1 ini adalah indeks terakhir atau paling atas
        
    def size(self):
        """
        Mendapatkan jumlah item dalam stack
        
        Returns:
            int: Jumlah item dalam stack
        """
        return len(self.items)
    
    def clear(self):
        """
        Mengosongkan stack
        """
        self.items = []
        
    def __str__(self):
        """
        Mengembalikan representasi string dari stack
        
        Returns:
            str: Representasi string dari stack
        """
        return str(self.items)

# Contoh penggunaan Stack dengan list == array
def test_stack_list():
    s = Stack()
    
    print("Apakah stack kosong?", s.is_empty())  # True
    
    print("\nMenambahkan elemen ke stack:")
    s.push(10)
    print("Stack setelah push(10):", s)
    
    s.push(20)
    print("Stack setelah push(20):", s)
    
    s.push(30)
    print("Stack setelah push(30):", s)
    
    print("\nUkuran stack:", s.size())  # 3
    
    print("\nMelihat elemen teratas stack:", s.peek())  # 30
    
    print("\nMengeluarkan elemen dari stack:")
    print("Pop:", s.pop())  # 30
    print("Stack setelah pop:", s)
    
    print("Pop:", s.pop())  # 20
    print("Stack setelah pop:", s)
    
    print("\nUkuran stack sekarang:", s.size())  # 1
    
    print("\nMengosongkan stack")
    s.clear()
    print("Apakah stack kosong?", s.is_empty())  # True


# Menjalankan pengujian
if __name__ == "__main__":
    test_stack_list()