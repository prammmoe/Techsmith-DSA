'''
Tugas Study Camp Techsmith - Algoritma dan Struktur Data

Deskripsi:
Di bawah ini adalah sebuah kode untuk mengimplementasikan sistem undo - redo yang sudah
dilengkapi dengan penjelasan masing-masing syntax atau bagian-bagian dari kode.

Todo:
Setelah mendapatkan penjelasan mengenai Stack, silakan Anda lengkapi bagian kode yang kurang
yang ditandai dengan komen dengan simbol "*". Setiap kode yang kurang sudah dilengkapi dengan clue.

Notes:
- self di Python adalah penanda bahwa suatu nilai adalah milik (atribut) dari suatu objek 
- Tanpa self, sebuah method tidak bisa mengakses atau mengubah atribut objek
- Ketika memanggil `editor` di bawah, objek `editor` diteruskan ke self

Good luck.
'''

class UndoRedoSystem:
    def __init__(self):
        self.undo_stack = []  # Menyimpan aksi yang sudah dilakukan
        self.redo_stack = []  # Menyimpan aksi yang di-undo

    def add_action(self, action):
        """Menambahkan aksi baru dan menghapus redo stack"""
        self.undo_stack.append(action)
        self.redo_stack.clear()  # Reset redo stack karena ada aksi baru
        print(f"Action added: {action}")

    def undo(self):
        """Mengembalikan ke aksi sebelumnya"""
        if not self.undo_stack:
            print("No actions to undo.")
            return
        action = self.undo_stack.pop()
        self.redo_stack.append(action)
        print(f"Undo: {action}")

    def redo(self):
        """Mengulang aksi yang di-undo"""
        if not self.redo_stack:
            print("No actions to redo.")
            return
        action = self.redo_stack.pop()
        self.undo_stack.append(action)
        print(f"Redo: {action}")

    def show_history(self):
        """Menampilkan aksi yang sudah dilakukan"""
        print("\n=== Action History ===")
        print(f"Undo Stack: {self.undo_stack}")
        print(f"Redo Stack: {self.redo_stack}")
        print("======================\n")

# Contoh penggunaan
editor = UndoRedoSystem()
editor.add_action("Type 'Hello'")
editor.add_action("Type 'World'")
editor.add_action("Delete 'World'")

editor.show_history()

editor.undo()  # Undo delete 'World'
editor.undo()  # Undo type 'World'
editor.show_history()

editor.redo()  # Redo type 'World'
editor.show_history()
