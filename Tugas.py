import tkinter as tk

def hasil_prediksi():
    # Menulis "Teknologi Informasi" ke dalam label hasil prediksi
    result_label.config(text="Prodi : Teknologi Informasi")

# Membuat jendela utama
root = tk.Tk()
root.title("Aplikasi Prediksi Prodi Pilihan") # Judul jendela
root.geometry('800x500')  # Ukuran jendela (lebar x tinggi)

# Label Judul Aplikasi
judul_label = tk.Label(root,
                        text='Prediksi Program Studi', # Teks judul
                        font=('Arial', '16'), # Font dan ukuran
                        fg='#007bff') # Warna teks
judul_label.pack(pady=20)  # Pakai padding atas dan bawah

# Frame untuk input nilai mata pelajaran
input_frame = tk.Frame(root) # Membuat frame untuk mengelompokkan input
input_frame.pack() # Menempatkan frame dalam jendela utama

# Input Nilai Mata Pelajaran
nilai_labels = [] # Daftar untuk menyimpan label nilai
nilai_entries = [] # Daftar untuk menyimpan entry nilai

for i in range(10):
    label_nilai = tk.Label(input_frame,
                            text=f'Nilai {i+1}: ',  # Label untuk setiap nilai
                            width=15, # Lebar label
                            anchor=tk.W) # Penjajaran teks ke kiri
    
    entry_nilai = tk.Entry(input_frame,
                            width=5) # Entry untuk memasukkan nilai
    
    label_nilai.grid(row=i, column=0) # Menempatkan label dalam grid
    entry_nilai.grid(row=i, column=1) # Menempatkan entry dalam grid
    
    nilai_labels.append(label_nilai) # Menyimpan label ke dalam daftar
    nilai_entries.append(entry_nilai) # Menyimpan entry ke dalam daftar

# Button Bertuliskan Hasil Prediksi 
button_hasil_prediksi = tk.Button(root,
                                text='Hasil Prediksi', # Teks tombol
                                command=lambda: hasil_prediksi()) # Menghubungkan tombol dengan fungsi hasil_prediksi
button_hasil_prediksi.place(relx=.40, rely=.8) # Menempatkan tombol di posisi relatif

# Label Luaran Hasil Prediksi 
result_label = tk.Label(root,
                        text='', # Teks awal kosong
                        font=('Arial', '14'), # Font dan ukuran untuk hasil
                        fg='#007bff') # Warna teks hasil
result_label.place(relx=.45, rely=.85) # Menempatkan label hasil di posisi relatif

# Memulai aplikasi Tkinter
root.mainloop()
