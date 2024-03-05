import mysql.connector
from tkinter import Tk, Label, Button, Entry, StringVar, messagebox, ttk, Toplevel
from tkcalendar import DateEntry 

def create_database_connection():
    return mysql.connector.connect(
        host="sql.freedb.tech",
        user="freedb_Moitoring_Bansos",
        password="KdEe5jVB*uEb$9G",
        database="distribusi_bansos"
    )

def create_table(cursor, table_name, columns):
    # Create table if not exists
    create_table_query = f"CREATE TABLE IF NOT EXISTS {table_name} ({columns})"
    cursor.execute(create_table_query)

# Fungsi untuk menampilkan tampilan depan saat aplikasi dimulai
root = Tk()
root.title("Aplikasi Distribusi Bansos")

# Inisialisasi database connection dan cursor
db = create_database_connection()
cursor = db.cursor()

login_window = None
login_attempts = [0]

# Inisialisasi tabel jika belum ada
create_table(cursor, "warga", "id INT AUTO_INCREMENT PRIMARY KEY, nama VARCHAR(255), alamat VARCHAR(255)")
create_table(cursor, "bansos", "id INT AUTO_INCREMENT PRIMARY KEY, nama_bansos VARCHAR(255), tanggal DATE, jumlah INT")
create_table(cursor, "transaksi", "id INT AUTO_INCREMENT PRIMARY KEY, id_warga INT, id_bansos INT, tanggal DATE, jumlah INT")

# Fungsi untuk menambahkan data warga
def tambah_data_warga(entry_nama, entry_alamat, treeview):
    nama = entry_nama.get()
    alamat = entry_alamat.get()
    query = "INSERT INTO warga (nama, alamat) VALUES (%s, %s)"
    cursor.execute(query, (nama, alamat))
    db.commit()
    messagebox.showinfo("Sukses", "Data warga berhasil ditambahkan")

    # Membersihkan input fields setelah menambahkan data
    entry_nama.delete(0, 'end')
    entry_alamat.delete(0, 'end')

    # Memperbarui tabel warga setelah membersihkan input fields
    refresh_tabel(treeview)

# Fungsi untuk menampilkan tampilan input data warga
def tampil_data_warga():
    # Buat toplevel untuk tampilan input data warga
    toplevel_warga = Toplevel(root)
    toplevel_warga.title("Input Data Warga")
    toplevel_warga.minsize(300, 200)  # Set a minimum size for the window

    # Style for buttons and labels
    style = ttk.Style()
    style.configure("TLabel", padding=5, font=('Helvetica', 10))
    style.configure("TButton", padding=5, font=('Helvetica', 10))

    # Label dan Entry untuk input data warga
    label_nama = ttk.Label(toplevel_warga, text="Nama:")
    label_alamat = ttk.Label(toplevel_warga, text="Alamat:")
    label_nama.grid(row=0, column=0, padx=10, pady=5, sticky="E")
    label_alamat.grid(row=1, column=0, padx=10, pady=5, sticky="E")

    entry_nama = ttk.Entry(toplevel_warga)
    entry_alamat = ttk.Entry(toplevel_warga)
    entry_nama.grid(row=0, column=1, padx=10, pady=5, sticky="W")
    entry_alamat.grid(row=1, column=1, padx=10, pady=5, sticky="W")

    # Inisialisasi treeview untuk warga
    tree_warga = ttk.Treeview(toplevel_warga, columns=("ID", "Nama", "Alamat"))
    tree_warga.heading("#0", text="ID")
    tree_warga.heading("#1", text="Nama")
    tree_warga.heading("#2", text="Alamat")
    tree_warga.grid(row=3, columnspan=2, padx=10, pady=10, sticky="NSEW")

    # Memperbarui tabel warga setelah inisialisasi treeview
    refresh_tabel(tree_warga)

    button_tambah = ttk.Button(toplevel_warga, text="Tambah Data Warga", command=lambda: tambah_data_warga(entry_nama, entry_alamat, tree_warga))
    button_tambah.grid(row=2, columnspan=2, pady=10)

    # Tombol untuk menutup tampilan input data warga
    button_tutup = ttk.Button(toplevel_warga, text="Tutup", command=toplevel_warga.destroy)
    button_tutup.grid(row=4, columnspan=2, pady=10)# Fungsi untuk memperbarui tabel data warga di treeview

def refresh_tabel(treeview):
    # Hapus semua item di dalam treeview
    children = treeview.get_children()
    if children:
        treeview.delete(*children)

    # Ambil data dari database warga
    query = "SELECT * FROM warga"
    cursor.execute(query)
    data_warga = cursor.fetchall()

    # Tampilkan data di treeview warga
    for warga in data_warga:
        treeview.insert("", "end", values=warga)

# Fungsi untuk menambahkan data bansos
def tambah_data_bansos(entry_bansos, entry_jumlah, tree_bansos):
    nama_bansos = entry_bansos.get()
    jumlah = entry_jumlah.get()
    query = "INSERT INTO bansos (nama_bansos, jumlah) VALUES (%s, %s)"
    cursor.execute(query, (nama_bansos, jumlah))
    db.commit()
    messagebox.showinfo("Sukses", "Data bansos berhasil ditambahkan")

    # Membersihkan input fields setelah menambahkan data
    entry_bansos.delete(0, 'end')
    entry_jumlah.delete(0, 'end')

    # Memperbarui tabel bansos setelah membersihkan input fields
    refresh_tabel_bansos(tree_bansos)

# Fungsi untuk menampilkan tampilan input data bansos
def tampil_data_bansos():
    # Buat toplevel untuk tampilan input data bansos
    toplevel_bansos = Toplevel(root)
    toplevel_bansos.title("Input Data Bansos")
    toplevel_bansos.minsize(300, 200)  # Set a minimum size for the window

    # Style for buttons and labels
    style = ttk.Style()
    style.configure("TLabel", padding=5, font=('Helvetica', 10))
    style.configure("TButton", padding=5, font=('Helvetica', 10))

    # Label dan Entry untuk input data bansos
    label_bansos = ttk.Label(toplevel_bansos, text="Nama Bansos:")
    label_jumlah = ttk.Label(toplevel_bansos, text="Jumlah:")
    label_bansos.grid(row=0, column=0, padx=10, pady=5, sticky="E")
    label_jumlah.grid(row=1, column=0, padx=10, pady=5, sticky="E")

    entry_bansos = ttk.Entry(toplevel_bansos)
    entry_jumlah = ttk.Entry(toplevel_bansos)
    entry_bansos.grid(row=0, column=1, padx=10, pady=5, sticky="W")
    entry_jumlah.grid(row=1, column=1, padx=10, pady=5, sticky="W")

    button_tambah_bansos = ttk.Button(toplevel_bansos, text="Tambah Data Bansos", command=lambda: tambah_data_bansos(entry_bansos, entry_jumlah, tree_bansos))
    button_tambah_bansos.grid(row=3, columnspan=2, pady=10)

    # Inisialisasi treeview untuk bansos
    tree_bansos = ttk.Treeview(toplevel_bansos, columns=("ID", "Nama Bansos", "Jumlah"))
    tree_bansos.heading("#0", text="ID")
    tree_bansos.heading("#1", text="Nama Bansos")
    tree_bansos.heading("#2", text="Jumlah")
    tree_bansos.grid(row=4, columnspan=2, padx=10, pady=10, sticky="NSEW")

    # Tombol untuk menutup tampilan input data bansos
    button_tutup = ttk.Button(toplevel_bansos, text="Tutup", command=toplevel_bansos.destroy)
    button_tutup.grid(row=5, columnspan=2, pady=10)

    # Memperbarui tabel bansos saat pertama kali tampilan dibuka
    refresh_tabel_bansos(tree_bansos)# Fungsi untuk memperbarui tabel data bansos di treeview

def refresh_tabel_bansos(tree_bansos):
    # Hapus semua item di dalam treeview bansos
    children = tree_bansos.get_children()
    if children:
        tree_bansos.delete(*children)

    # Ambil data dari database bansos
    query = "SELECT id, nama_bansos,jumlah FROM bansos"
    cursor.execute(query)
    data_bansos = cursor.fetchall()

    # Tampilkan data di treeview bansos
    for bansos in data_bansos:
        tree_bansos.insert("", "end", values=bansos)
# Function to fetch jumlah from bansos based on the selected ID Jenis Bansos
def fetch_jumlah_from_bansos(selected_bansos_id):
    query = "SELECT jumlah FROM bansos WHERE id = %s"
    cursor.execute(query, (selected_bansos_id,))
    jumlah = cursor.fetchone()
    return jumlah[0] if jumlah else 0

# Fungsi untuk menambahkan data transaksi
def tambah_data_transaksi(entry_id_warga, entry_id_jenis_bansos, entry_tanggal, tree_transaksi):
    tanggal = entry_tanggal
    selected_bansos_id = entry_id_jenis_bansos.split('-')
    selected_warga_id = entry_id_warga.split('-')
    print(tanggal)
      # Extracting the ID from "ID - Nama"
    jumlah_terima = fetch_jumlah_from_bansos(selected_bansos_id[0])
    query = "INSERT INTO transaksi (id_warga, id_jenis_bansos, tanggal_penerimaan, jumlah_terima) VALUES (%s, %s, %s, %s)"
    cursor.execute(query, (selected_warga_id[0], selected_bansos_id[0], tanggal, jumlah_terima))
    db.commit()
    messagebox.showinfo("Sukses", "Data transaksi berhasil ditambahkan")

    # Memperbarui tabel transaksi setelah membersihkan input fields
    refresh_tabel_transaksi(tree_transaksi)

# Fungsi untuk memperbarui tabel data transaksi di treeview
def refresh_tabel_transaksi(tree_transaksi):
    # Hapus semua item di dalam treeview transaksi
    for row in tree_transaksi.get_children():
        tree_transaksi.delete(row)

    # Ambil data dari database transaksi
    query = "SELECT transaksi.id, warga.nama, bansos.nama_bansos, transaksi.tanggal_penerimaan, transaksi.jumlah_terima FROM transaksi JOIN bansos ON bansos.id = transaksi.id_jenis_bansos JOIN warga ON warga.id = transaksi.id_warga"
    cursor.execute(query)
    data_transaksi = cursor.fetchall()

    # Tampilkan data di treeview transaksi
    for transaksi in data_transaksi:
        tree_transaksi.insert("", "end", values=transaksi)

# Fungsi untuk menampilkan tampilan input data transaksi
def tampil_data_transaksi():
    # Buat toplevel untuk tampilan input data transaksi
    toplevel_transaksi = Toplevel(root)
    toplevel_transaksi.title("Input Data Transaksi")
    toplevel_transaksi.minsize(400, 300)  # Set a minimum size for the window

    # Style for buttons and labels
    style = ttk.Style()
    style.configure("TLabel", padding=5, font=('Helvetica', 10))
    style.configure("TButton", padding=5, font=('Helvetica', 10))

    # Label dan Combobox untuk input data transaksi
    label_id_warga = ttk.Label(toplevel_transaksi, text="ID Warga:")
    label_id_jenis_bansos = ttk.Label(toplevel_transaksi, text="ID Jenis Bansos:")
    label_tanggal = ttk.Label(toplevel_transaksi, text="Tanggal Penerimaan:")
    label_id_warga.grid(row=0, column=0, padx=10, pady=5, sticky="E")
    label_id_jenis_bansos.grid(row=1, column=0, padx=10, pady=5, sticky="E")
    label_tanggal.grid(row=2, column=0, padx=10, pady=5, sticky="E")

    query = "SELECT * FROM warga"
    cursor.execute(query)
    data_warga = cursor.fetchall()

    queryBansos = "SELECT * FROM bansos"
    cursor.execute(queryBansos)
    data_bansos = cursor.fetchall()

    # Combobox untuk memilih ID Warga
    warga_options = [f"{warga[0]}-{warga[1]}" for warga in data_warga]  # Ganti data_warga dengan data yang sesuai
    combo_id_warga = ttk.Combobox(toplevel_transaksi, values=warga_options)
    combo_id_warga.grid(row=0, column=1, padx=10, pady=5, sticky="W")

    # Combobox untuk memilih ID Jenis Bansos
    bansos_options = [f"{bansos[0]}-{bansos[1]}" for bansos in data_bansos]  # Ganti data_bansos dengan data yang sesuai
    combo_id_jenis_bansos = ttk.Combobox(toplevel_transaksi, values=bansos_options)
    combo_id_jenis_bansos.grid(row=1, column=1, padx=10, pady=5, sticky="W")

    # DateEntry untuk memilih tanggal
    entry_tanggal = DateEntry(toplevel_transaksi, width=12, background='darkblue', foreground='white', borderwidth=2)
    entry_tanggal.grid(row=2, column=1, padx=10, pady=5, sticky="W")

    button_tambah_transaksi = ttk.Button(toplevel_transaksi, text="Tambah Data Transaksi", command=lambda: tambah_data_transaksi(combo_id_warga.get(), combo_id_jenis_bansos.get(), entry_tanggal.get_date(), tree_transaksi))
    button_tambah_transaksi.grid(row=3, columnspan=2, pady=10)

    tree_transaksi = ttk.Treeview(toplevel_transaksi, columns=("ID", "Nama Warga", "Jenis Bansos", "Tanggal", "Jumlah"))
    tree_transaksi.heading("#0", text="ID")
    tree_transaksi.heading("#1", text="Nama Warga")
    tree_transaksi.heading("#2", text="Jenis Bansos")
    tree_transaksi.heading("#3", text="Tanggal")
    tree_transaksi.heading("#4", text="Jumlah")
    tree_transaksi.grid(row=4, columnspan=2, padx=10, pady=10, sticky="NSEW")

    # Tombol untuk menutup tampilan input data transaksi
    button_tutup = ttk.Button(toplevel_transaksi, text="Tutup", command=toplevel_transaksi.destroy)
    button_tutup.grid(row=5, columnspan=2, pady=10)

    refresh_tabel_transaksi(tree_transaksi)

# Function to validate login credentials
def validate_login(username, password, login_attempts):
    # For simplicity, hardcoding the admin credentials
    correct_username = "admin"
    correct_password = "admin"

    if username == correct_username and password == correct_password:
        return True
    else:
        login_attempts[0] += 1
        messagebox.showwarning("Login Failed", f"Incorrect credentials. Attempts remaining: {3 - login_attempts[0]}")
        if login_attempts[0] >= 3:
            messagebox.showerror("Login Failed", "Too many incorrect attempts. Exiting the program.")
            root.destroy()
        return False

# Function to handle the login process
def login():
    global login_window

    login_window = root
    login_window.title("Login")

    # Style for labels, buttons, and entry widgets
    style = ttk.Style()
    style.configure("TLabel", padding=(0, 5), font=('Helvetica', 12))
    style.configure("TButton", padding=5, font=('Helvetica', 12))
    style.configure("TEntry", padding=5, font=('Helvetica', 12))

    # Label and Entry for username
    label_username = ttk.Label(login_window, text="Username:")
    label_username.grid(row=0, column=0, padx=10, pady=5, sticky="E")
    entry_username = ttk.Entry(login_window)
    entry_username.grid(row=0, column=1, padx=10, pady=5, sticky="W")

    # Label and Entry for password
    label_password = ttk.Label(login_window, text="Password:")
    label_password.grid(row=1, column=0, padx=10, pady=5, sticky="E")
    entry_password = ttk.Entry(login_window, show="*")
    entry_password.grid(row=1, column=1, padx=10, pady=5, sticky="W")

    # Button to submit login
    button_login = ttk.Button(login_window, text="Login", command=lambda: check_login(entry_username.get(), entry_password.get()))
    button_login.grid(row=2, columnspan=2, pady=10)

# Function to check login credentials and decide whether to show the main interface
def check_login(username, password):
    global login_attempts

    if validate_login(username, password, login_attempts):
        login_attempts = [0] 
        tampil_tampilan_depan() # Call the function to initialize the main interface
    elif login_attempts[0] >= 3:
        messagebox.showerror("Error", "Terlalu banyak percobaan")
        root.destroy()


# Fungsi untuk menampilkan tampilan depan
def tampil_tampilan_depan():
    global login_window
    toplevel_home = root

    # Hapus semua widget di dalam toplevel_home
    for widget in toplevel_home.winfo_children():
        widget.destroy()

    # Set background color
    toplevel_home.configure(bg="#f0f0f0")

    # Set window title
    toplevel_home.title("Aplikasi Distribusi Bansos")

    # Tentukan lebar dan tinggi jendela utama
    window_width = 600
    window_height = 400

    # Set ukuran jendela utama menggunakan geometry()
    toplevel_home.geometry(f"{window_width}x{window_height}")

    # Font style for buttons
    button_font = ("Helvetica", 14)

    # Tombol untuk data warga
    button_data_warga = Button(toplevel_home, text="Data Warga", command=tampil_data_warga, font=button_font, padx=10, pady=5, bg="#4CAF50", fg="white")
    button_data_warga.pack(pady=20)

    # Tombol untuk data bansos
    button_data_bansos = Button(toplevel_home, text="Data Bansos", command=tampil_data_bansos, font=button_font, padx=10, pady=5, bg="#008CBA", fg="white")
    button_data_bansos.pack(pady=20)

    # Tombol untuk data transaksi
    button_data_transaksi = Button(toplevel_home, text="Data Transaksi", command=tampil_data_transaksi, font=button_font, padx=10, pady=5, bg="#f44336", fg="white")
    button_data_transaksi.pack(pady=20)

login()

root.mainloop()
