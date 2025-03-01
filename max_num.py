# Function untuk mencari angka tertinggi di dalam deret
def find_max_num(nums):
    
    # Conditional checking apakah nums kosong atau tidak
    if not nums:
        # Kalau nums kosong, return -1
        return -1;

    # Variabel untuk asumsikan angka terbesar berada di deret pertama
    max_num = nums[0]
    # Looping ke dalam deret 
    for num in nums:
        # Conditional checking apakah angka yang diiterasikan > dari angka terbesar sementara
        if num > max_num:
            # Jika angka yang sedang diiterasikan lebih besar, maka atur angka terbesar ke angka tersebut
            max_num = num

    # Kembalikan angka terbesar yang disimpan di variabel max_num
    return max_num

# Inisialisasi deret angka
nums = [100, 2000, 5, 20, 100]

# Variabel untuk menyimpan nilai yang dikembalikan function find_max_num
find_max = find_max_num(nums)
# Cetak angka tertinggi
print(f"The highest number is: {find_max}")
