import tkinter as tk
from tkinter import messagebox

# Fungsi untuk menampilkan hasil prediksi
def hasil_prediksi():
    try:
        # Mengecek setiap input apakah berupa angka
        for entry in entries:
            if not entry.get().isdigit():
                raise ValueError("Semua nilai mata pelajaran harus berupa angka.")
        
        # Jika semua input valid, tampilkan hasil prediksi
        hasil_label.config(text="Prodi: Teknologi Informasi")
    except ValueError as e:
        # Menampilkan pesan error jika ada input yang bukan angka
        messagebox.showerror("Input Error", str(e))

# Membuat window utama
root = tk.Tk()
root.title("Aplikasi Prediksi Prodi Pilihan")

# Label judul
judul_label = tk.Label(root, text="Aplikasi Prediksi Prodi Pilihan", font=("Arial", 16))
judul_label.grid(row=0, column=0, columnspan=2, pady=10)

# Membuat label dan entry untuk 10 nilai mata pelajaran
entry_labels = []
entries = []
for i in range(10):
    label = tk.Label(root, text=f"Nilai Mata Pelajaran {i + 1}:")
    label.grid(row=i + 1, column=0, padx=10, pady=5, sticky="e")
    entry_labels.append(label)

    entry = tk.Entry(root)
    entry.grid(row=i + 1, column=1, padx=10, pady=5)
    entries.append(entry)

# Button untuk menampilkan hasil prediksi
prediksi_button = tk.Button(root, text="Hasil Prediksi", command=hasil_prediksi)
prediksi_button.grid(row=11, column=0, columnspan=2, pady=10)

# Label hasil prediksi
hasil_label = tk.Label(root, text="", font=("Arial", 14))
hasil_label.grid(row=12, column=0, columnspan=2, pady=10)

# Menjalankan mainloop
root.mainloop()