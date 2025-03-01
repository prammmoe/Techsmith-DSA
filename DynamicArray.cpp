#include <iostream>
#include <vector>

using namespace std;

int main() {
    // Inisialisasi dynamic array menggunakan STL Vector
    vector<int> arr = {2, 4, 6, 8, 10}; // panjangnya 5

    // Tambah satu elemen di belakang
    arr.push_back(5);

    // Looping untuk print
    for (int i = 0; i < arr.size(); i++) {
        cout << arr[i] << endl;
    }

    // Atau bisa juga gini ngeprintnya
    for (int num : arr) {
        cout << num << endl;
    }
    return 0;
}