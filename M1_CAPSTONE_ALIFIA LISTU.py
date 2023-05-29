''' CAPSTONE MODUL 1 : RENTAL MOBIL - ALIFIA LISTU SAMATHA - JCDS BANDUNG '''

# untuk menghasilkan table yang lebih cantik dan rapih (values, headers)
from tabulate import tabulate
# untuk membuat teks jadi berwarna (Fore.WARNA + 'teks' + Style.RESET_ALL)
from colorama import Fore, Style

# memakai nested dictionary karena lebih mudah untuk mengakses key dan valuesnya
headers = ['Kode', 'Merk', 'Tipe', 'Kapasitas', 'Transmisi', 'Tahun', 'Jumlah', 'Jenis Sewa', 'Harga (12 Jam)']
data_mobil = {
              'M01' : {
                        'Merk'            : 'Toyota Camry',
                        'Tipe'            : 'Sedan',
                        'Kapasitas'       : '4 Orang',
                        'Transmisi'       : 'Otomatis',
                        'Tahun'           : 2018,
                        'Jumlah'          : '1 Unit',
                        'Jenis Sewa'      : 'Supir',
                        'Harga'           : 1000000
                      },    
              'M02' : {
                        'Merk'            : 'Daihatsu Xenia',
                        'Tipe'            : 'MPV',
                        'Kapasitas'       : '7 orang',
                        'Transmisi'       : 'Manual',
                        'Tahun'           : 2020,
                        'Jumlah'          : '3 Unit',
                        'Jenis Sewa'      : 'Supir/Lepas Kunci',
                        'Harga'           : 200000        
                      },
              'M03' : {
                        'Merk'            : 'Toyota Rush',
                        'Tipe'            : 'SUV',
                        'Kapasitas'       : '6 Orang',
                        'Transmisi'       : 'Otomatis',
                        'Tahun'           : 2017,
                        'Jumlah'          : '2 Unit',
                        'Jenis Sewa'      : 'Supir',
                        'Harga'           : 650000        
                      },
              'M04' : {
                        'Merk'            : 'Toyota Yaris',
                        'Tipe'            : 'Hatchback',
                        'Kapasitas'       : '4 Orang',
                        'Transmisi'       : 'Manual',
                        'Tahun'           : 2022,
                        'Jumlah'          : '2 Unit',
                        'Jenis Sewa'      : 'Supir/Lepas Kunci',
                        'Harga'           : 450000        
                      },
              'M05' : {
                        'Merk'            : 'Mitsubishi Pajero',
                        'Tipe'            : 'MPV',
                        'Kapasitas'       : '7 Orang',
                        'Transmisi'       : 'Manual',
                        'Tahun'           : 2013,
                        'Jumlah'          : '2 Unit',
                        'Jenis Sewa'      : 'Supir',
                        'Harga'           : 550000        
                      }
}

# fungsi untuk menampilkan menu utama -> menu awal yang dilihat saat di run
def menu_utama():
    while True:
        print()
        print('-'*40)
        print(' SELAMAT DATANG DI BANDUNG RENTAL MOBIL')
        print('-'*40)
        print('''
    1. Daftar Mobil
    2. Mode Pesewa
    3. Mode Penyewa
    4. Keluar Program\n''')
        menu = input('Pilih Menu : ')
        if menu.isdigit() == True:
            menu = int(menu)
        else:
            print(Fore.RED + '\nPERINGATAN! MASUKKAN INPUT HANYA BERUPA ANGKA.' + Style.RESET_ALL)
            input("\nTekan Enter untuk Kembali ke Menu Utama")
            menu_utama()
        if menu == 1:
            print()
            lihat_mobil()
        elif menu == 2:
            print()
            mode_pesewa()
        elif menu == 3:
            mode_penyewa()
        elif menu == 4:
            print()
            print('== Terimakasih Telah Menggunakan Aplikasi BANDUNG RENTAL MOBIL! ==\n')
            exit()
        else:
            print(Fore.RED + '\nPERINGATAN! MENU TIDAK ADA.' + Style.RESET_ALL)
        input("\nTekan Enter untuk Kembali ke Menu Utama")
        menu_utama()    

# fungsi untuk menampilkan menu daftar mobil -> menampilkan, mencari, filter, dan sorting data mobil
def lihat_mobil():
    print('-'*16)
    print('| DAFTAR MOBIL |')
    print('-'*16)
    print('''\n    1. Tampilkan Semua Daftar Mobil
    2. Tampilkan Daftar Mobil Berdasarkan Kode
    3. Cari Merk Mobil
    4. Filter Mobil
    5. Sorting Mobil
    6. Kembali ke Menu Utama
    ''')
    menu = input('Pilih Menu : ')
    # jika inputan yang dimasukan adalah digit, maka str akan di convert ke int
    if menu.isdigit() == True:
        menu = int(menu)
    else:
        print(Fore.RED + '\nPERINGATAN! MASUKKAN INPUT HANYA BERUPA ANGKA.' + Style.RESET_ALL)
        input("\nTekan Enter untuk Kembali ke Daftar Mobil")
        print()
        lihat_mobil()
    # pilihan menu untuk melihat semua daftar mobil
    if menu == 1:
        print()
        print('-'*37)
        print('| DAFTAR MOBIL > SEMUA DAFTAR MOBIL |')
        print('-'*37)
        daftar_mobil()
        input("Tekan Enter untuk Kembali ke Daftar Mobil")
        print()
        lihat_mobil()
    # pilihan menu untuk melihat daftar mobil tertentu sesuai dengan kode yang diinput
    elif menu == 2:
        print()
        print('-'*40)
        print('| DAFTAR MOBIL > DAFTAR MOBIL TERTENTU |')
        print('-'*40)
        tampil_kode()
        input("Tekan Enter untuk Kembali ke Daftar Mobil")
        print()
        lihat_mobil()
    # pilihan menu untuk mencari merk mobil
    elif menu == 3:
        print()
        print('-'*34)
        print('| DAFTAR MOBIL > CARI MERK MOBIL |')
        print('-'*34)
        cari_mobil()
        input("Tekan Enter untuk Kembali ke Daftar Mobil")
        print()
        lihat_mobil()
    # pilihan menu untuk filter mobil
    elif menu == 4:
        print()
        print('-'*31)
        print('| DAFTAR MOBIL > FILTER MOBIL |')
        print('-'*31)
        filter_mobil()
        input("Tekan Enter untuk Kembali ke Daftar Mobil")
        print()
        lihat_mobil()
    # pilihan menu untuk sorting mobil
    elif menu == 5:
        print()
        print('-'*32)
        print('| DAFTAR MOBIL > SORTING MOBIL |')
        print('-'*32)
        sorting_mobil()
        input("Tekan Enter untuk Kembali ke Daftar Mobil")
        print()
        lihat_mobil()
    # pilihan menu untuk kembali ke menu utama
    elif menu == 6:
        menu_utama()
    else:
        print(Fore.RED + '\nPERINGATAN! MENU TIDAK ADA.' + Style.RESET_ALL)
        input("\nTekan Enter untuk Kembali ke Daftar Mobil\n")
        lihat_mobil()

# fungsi untuk menampilkan semua data mobil
def daftar_mobil():
    empty = {}
    # kalau data empty / tidak ada data, akan ada warning sign bahwa data mobil kosong
    if data_mobil == empty:
        print(Fore.RED + 'PERINGATAN! DATA MOBIL KOSONG. SILAHKAN TAMBAH DATA MOBIL.\n' + Style.RESET_ALL)
    else:
        print('\n== DAFTAR MOBIL ==\n')
        # values diambil dari key dan values dari data_mobil
        # *values -> merk, tipe, kapasitas, dll, values() -> kita ambil values dari *values
        # untuk ekstrak key, values harus dgn for loop key, values in data_mobil.items()
        values = [[key, *values.values()] for key, values in data_mobil.items()]
        print_table(values)

# fungsi untuk menampilkan data mobil tertentu sesuai dengan kode
def tampil_kode():
    empty = {}
    # kalau data empty / tidak ada data, akan ada warning sign bahwa data mobil kosong
    if data_mobil == empty:
        print(Fore.RED + '\nPERINGATAN! DATA MOBIL KOSONG. SILAHKAN TAMBAH DATA MOBIL.\n' + Style.RESET_ALL)
    else:
        kode = input('\nMasukkan Kode Mobil: ').title()
        print()
        # kode harus berawalan huruf M dan diakhiri dengan angka, kalau tidak akan ada warning sign
        if not kode.startswith('M') or kode[1:].isdigit() == False:
            print(Fore.RED + 'PERINGATAN! KODE HARUS DIAWALI DENGAN HURUF "M" DAN DIAKHIRI DENGAN ANGKA.' + Style.RESET_ALL)
            tampil_kode()
        else:
            if kode in list(data_mobil.keys()):
                print('== DAFTAR MOBIL ==\n')
                # ambil index data sesuai dengan kode, misal kode = m01 -> index kode m01 ada di index ke-0
                idx = list(data_mobil.keys()).index(kode)
                # values = key dan values sesuai dengan index di atas -> data index ke-0
                values = [[[key, *values.values()] for key, values in data_mobil.items()][idx]]
                # lanjut ke fungsi print table
                print_table(values)
                print()
            else:
                # jika tidak ada kode dalam data, maka akan ada warning sign
                print(Fore.RED + 'PERINGATAN! TIDAK ADA KODE MOBIL TERSEBUT DALAM DATA.' + Style.RESET_ALL)
                tampil_kode()

# fungsi untuk mencari data sesui dengan merk mobil
def cari_mobil():
    empty = {}
    # kalau data empty / tidak ada data, akan ada warning sign bahwa data mobil kosong
    if data_mobil == empty:
        print(Fore.RED + '\nPERINGATAN! DATA MOBIL KOSONG. SILAHKAN TAMBAH DATA MOBIL.\n' + Style.RESET_ALL)
        input("Tekan Enter untuk Kembali ke Daftar Mobil")
        print()
        lihat_mobil()
    else:
        # inputan cari diubah menjadi title agar dapat mencari kesamaan pada data
        cari = input('\nMasukkan Merk Mobil yang dicari : ').title()
        # ambil list value dari merk
        val_merk = [value['Merk'] for key, value in data_mobil.items()]
        list_idx = []
        count = 0
        # untuk semua item ada pada list value merk
        for item in val_merk:
            # jika cari (merk mobil yang diinput) ada pada list value merk
            if cari in item:
                # ambil index item dari val_merk
                idx = val_merk.index(item)
                # ambil key, values berdasarkan index diatas
                values = [[key, *values.values()] for key, values in data_mobil.items()][idx]
                # values di append agar bisa menjadi list (krn bisa lebih dari 1 hasil)
                list_idx.append(values)
                # fungsi count untuk menandai apakah merk yg dicari muncul lebih dari 1 atau kurang dari 1 (0)
                count += 1
            # diberikan kemungkinan juga jika user input kata dmn di data bukan huruf pertama -> misal oyo dari Toyota
            elif cari.lower() in item:
                idx = val_merk.index(item)
                values = [[key, *values.values()] for key, values in data_mobil.items()][idx]
                list_idx.append(values)
                count += 1
        else:
            # jika merk yg dicari hasilnya 0, maka akan ada peringatan mobil tidak ada
            if count < 1:
                print(Fore.RED + '\nPERINGATAN! TIDAK ADA MERK MOBIL TERSEBUT.' + Style.RESET_ALL)
        print('\n== HASIL PENCARIAN MOBIL ==\n')
        # lanjut ke print table dengan membawa values = list_idx
        print_table(values=list_idx)         

# fungsi untuk filter mobil
def filter_mobil():
    empty = {}
    count = 0
    # kalau data empty / tidak ada data, akan ada warning sign bahwa data mobil kosong
    if data_mobil == empty:
        print(Fore.RED + '\nPERINGATAN! DATA MOBIL KOSONG. SILAHKAN TAMBAH DATA MOBIL.\n' + Style.RESET_ALL)
        input("Tekan Enter untuk Kembali ke Daftar Mobil")
        print()
        lihat_mobil()
    else:
        # user harus memilih ingin filter berdasarkan apa
        print('''\nFilter Berdasarkan:\n
        1. Tipe Mobil
        2. Kapasitas Mobil
        3. Transmisi Mobil
        4. Tahun Keluaran Mobil
        5. Jenis Sewa Mobil
        6. Harga Mobil
        7. Kembali ke Daftar Mobil\n''')
        menu = input('Pilih Menu : ')
        # pastikan inputan user berupa digit -> lalu str akan diconvert ke int
        if menu.isdigit() == True:
            menu = int(menu)
        else:
            print(Fore.RED + '\nPERINGATAN! MASUKKAN INPUT HANYA BERUPA ANGKA.' + Style.RESET_ALL)
            input("\nTekan Enter untuk Kembali ke Filter Mobil")
            filter_mobil()
        # menu untuk filter berdasarkan tipe mobil
        if menu == 1:
            # krn menu masih berbentuk int, akan diubah dulu ke nama kolom sesuai dengan pilihan
            menu = 'Tipe'
            kolom = input('\nMasukkan Tipe Mobil : ').title()
             # ambil list value dari tipe
            val = [value[menu] for key, value in data_mobil.items()]
            # untuk setiap item pada list value tipe
            for item in val:
                # jika kolom (nama tipe mobil) yang diinput ada pada item
                if kolom in item:
                    # lanjut ke fungsi filter_str menggunakan param menu dan kolom
                    filter_str(menu,kolom)
                # cek juga jika ada nama tipe mobil yang .upper -> SUV, MPV
                elif kolom.upper() in item:
                    filter_str(menu,kolom.upper())
            else:
                print(Fore.RED + f'\nPERINGATAN! TIDAK ADA DATA DENGAN {menu.upper()} TERSEBUT.' + Style.RESET_ALL)
                filter_str(menu,kolom)
        # menu untuk filter berdasarkan kapasitas mobil
        elif menu == 2:
            menu = 'Kapasitas'
            kolom = input('\nMasukkan Kapasitas Mobil : ')
            # jika inputan yang dimasukan adalah digit, maka str akan di convert ke int
            if kolom.isdigit() == True:
                kolom = int(kolom)
                filter_int(menu, kolom)
            else:
                print(Fore.RED + '\nPERINGATAN! MASUKKAN INPUT HANYA BERUPA ANGKA.' + Style.RESET_ALL)
                input("\nTekan Enter untuk Kembali ke Filter Mobil")
                filter_mobil()
        # menu untuk filter berdasarkan transmisi mobil
        elif menu == 3:
            menu = 'Transmisi'
            kolom = input('\nMasukkan Jenis Transmisi Mobil : ').title()
            # untuk setiap item pada list value transmisi
            val = [value[menu] for key, value in data_mobil.items()]
            # untuk setiap item pada list value transmisi
            for item in val:
                # jika kolom (jenis transmisi mobil) yang diinput ada pada item
                if kolom in item:
                    # lanjut ke fungsi filter_str menggunakan param menu dan kolom
                    filter_str(menu,kolom)
                    # fungsi count untuk menandai apakah transmisi yg dicari muncul lebih dari 1 atau kurang dari 1 (0)
                    count += 1
            else:
                # jika transmisi yg dicari hasilnya 0, maka akan ada peringatan mobil tidak ada
                if count < 1:
                    print(Fore.RED + f'\nPERINGATAN! TIDAK ADA DATA DENGAN {menu.upper()} TERSEBUT.' + Style.RESET_ALL)
                    filter_str(menu,kolom)
        # menu untuk filter berdasarkan tahun keluaran mobil
        elif menu == 4:
            menu = 'Tahun'
            kolom = input('\nMasukkan Minimal Tahun Keluaran Mobil : ')
            # jika inputan yang dimasukan adalah digit, maka str akan di convert ke int
            if kolom.isdigit() == True:
                kolom = int(kolom)
                filter_int(menu, kolom)
            else:
                print(Fore.RED + '\nPERINGATAN! MASUKKAN INPUT HANYA BERUPA ANGKA.' + Style.RESET_ALL)
                input("\nTekan Enter untuk Kembali ke Filter Mobil")
                filter_mobil()
        # menu untuk filter berdasarkan jenis sewa mobil
        elif menu == 5:
            menu = 'Jenis Sewa'
            kolom = input('\nMasukkan Jenis Sewa Mobil (Supir/Lepas Kunci): ').title()
            # untuk setiap item pada list value jenis sewa
            val = [value[menu] for key, value in data_mobil.items()]
            # untuk setiap item pada list value jenis sewa
            for item in val:
                # jika kolom (jenis sewa) yang diinput ada pada item
                if kolom in item:
                    # lanjut ke fungsi filter_str menggunakan param menu dan kolom
                    filter_str(menu,kolom)
                    # fungsi count untuk menandai apakah jenis sewa yg dicari muncul lebih dari 1 atau kurang dari 1 (0)
                    count += 1
            else:
                # jika jenis sewa yg dicari hasilnya 0, maka akan ada peringatan mobil tidak ada
                if count < 1:
                    print(Fore.RED + f'\nPERINGATAN! TIDAK ADA DATA DENGAN {menu.upper()} TERSEBUT.' + Style.RESET_ALL)
                    filter_str(menu,kolom)
        # menu untuk filter berdasarkan harga mobil
        elif menu == 6:
            menu = 'Harga'
            kolom = input('\nMasukkan Minimal Harga Sewa Mobil : ')
            # jika inputan yang dimasukan adalah digit, maka str akan di convert ke int
            if kolom.isdigit() == True:
                kolom = int(kolom)
                filter_int(menu, kolom)
            else:
                print(Fore.RED + '\nPERINGATAN! MASUKKAN INPUT HANYA BERUPA ANGKA.' + Style.RESET_ALL)
                input("\nTekan Enter untuk Kembali ke Filter Mobil")
                filter_mobil()
        # menu untuk kembali ke daftar mobil
        elif menu == 7:
            print()
            lihat_mobil()
        else:
            print(Fore.RED + '\nPERINGATAN! MENU TIDAK ADA.' + Style.RESET_ALL)
            input("\nTekan Enter untuk Kembali ke Filter Mobil\n")
            filter_mobil()

# fungsi untuk print tabel jika inputan berupa string
def filter_str(menu, kolom):
    # jika kolom (jenis sewa) diisi lepas kunci -> yang keluar semua daftar yg kolom jenis sewanya Supir/Lepas Kunci
    if kolom == 'Lepas Kunci':
        values = [[key, *value.values()] for key, value in data_mobil.items() if value[f'{menu}'] == 'Supir/Lepas Kunci']
        print('\n== HASIL FILTER MOBIL ==\n')
        print_table(values)
        input("\nTekan Enter untuk Kembali ke Filter Mobil")
        filter_mobil()
    # else daftarnya dikeluarkan sesuai dengan inputan kolom yang diisi
    else:
        values = [[key, *value.values()] for key, value in data_mobil.items() if value[f'{menu}'] == kolom]
        print('\n== HASIL FILTER MOBIL ==\n')
        print_table(values)
        input("\nTekan Enter untuk Kembali ke Filter Mobil")
        filter_mobil()

# fungsi untuk print tabel jika inputan berupa integer
def filter_int(menu, kolom):
    # jika menu yg dipilih kapasitas
    if menu == 'Kapasitas':
        # values yang dipilih jika index ke 0 dari hasil split '(angka) Orang' -> angka >= kolom
        values = [[key, *value.values()] for key, value in data_mobil.items() if int(value[f'{menu}'].split()[0]) >= kolom]
        print('\n== HASIL FILTER MOBIL ==\n')
        print_table(values)
        input("\nTekan Enter untuk Kembali ke Filter Mobil")
        filter_mobil()
    else:
        # else value integer >= kolom
        values = [[key, *value.values()] for key, value in data_mobil.items() if value[f'{menu}'] >= kolom]
        print('\n== HASIL FILTER MOBIL ==\n')
        print_table(values)
        input("\nTekan Enter untuk Kembali ke Filter Mobil")
        filter_mobil()

# fungsi untuk sorting mobil
def sorting_mobil():
    empty = {}
    # kalau data empty / tidak ada data, akan ada warning sign bahwa data mobil kosong
    if data_mobil == empty:
        print(Fore.RED + '\nPERINGATAN! DATA MOBIL KOSONG. SILAHKAN TAMBAH DATA MOBIL.\n' + Style.RESET_ALL)
        input("Tekan Enter untuk Kembali ke Daftar Mobil")
        print()
        lihat_mobil()
    # pilihan sorting berdasarkan kolom apa
    else:
        print('''\nSorting Berdasarkan:\n
        1. Merk Mobil
        2. Kapasitas Mobil
        3. Transmisi Mobil
        4. Tahun Keluaran Mobil
        5. Jenis Sewa Mobil
        6. Harga Mobil
        7. Kembali ke Daftar Mobil\n''')
        menu = input('Pilih Menu : ')
        # pastikan inputan user berupa digit -> lalu str akan diconvert ke int
        if menu.isdigit() == True:
            menu = int(menu)
        else:
            print(Fore.RED + '\nPERINGATAN! MASUKKAN INPUT HANYA BERUPA ANGKA.' + Style.RESET_ALL)
            input("\nTekan Enter untuk Kembali ke Sorting Mobil")
            sorting_mobil()
        if menu == 1:
            # krn menu masih berbentuk int, akan diubah dulu ke nama kolom sesuai dengan pilihan
            menu = 'Merk'
            proses_sorting(menu)
        elif menu == 2:
            # krn menu masih berbentuk int, akan diubah dulu ke nama kolom sesuai dengan pilihan
            menu = 'Kapasitas'
            proses_sorting(menu)
        elif menu == 3:
            # krn menu masih berbentuk int, akan diubah dulu ke nama kolom sesuai dengan pilihan
            menu = 'Transmisi'
            proses_sorting(menu)
        elif menu == 4:
            # krn menu masih berbentuk int, akan diubah dulu ke nama kolom sesuai dengan pilihan
            menu = 'Tahun'
            proses_sorting(menu)
        elif menu == 5:
            # krn menu masih berbentuk int, akan diubah dulu ke nama kolom sesuai dengan pilihan
            menu = 'Jenis Sewa'
            proses_sorting(menu)
        elif menu == 6:
            # krn menu masih berbentuk int, akan diubah dulu ke nama kolom sesuai dengan pilihan
            menu = 'Harga'
            proses_sorting(menu)
        elif menu == 7:
            print()
            lihat_mobil()
        else:
            print(Fore.RED + '\nPERINGATAN! MENU TIDAK ADA.' + Style.RESET_ALL)
            input("\nTekan Enter untuk Kembali ke Sorting Mobil\n")
            sorting_mobil()

# fungsi untuk proses sorting
def proses_sorting(menu):
    # disini user akan ditanya lagi terkait jenis sorting (ascending/descending)
    print('''\nJenis Sorting:\n
        1. Ascending
        2. Descending
        3. Kembali ke Sorting Mobil\n''')
    pilih = input('Pilih Menu : ')
    # pastikan inputan user berupa digit -> lalu str akan diconvert ke int
    if pilih.isdigit() == True:
        pilih = int(pilih)
    else:
        print(Fore.RED + '\nPERINGATAN! MASUKKAN INPUT HANYA BERUPA ANGKA.' + Style.RESET_ALL)
        input("\nTekan Enter untuk Kembali ke Jenis Sorting")
        proses_sorting(menu)
    # jika pilih 1 akan lanjut ke fungsi proses sorting ascending
    if pilih == 1:
        proses_sorting_asc(menu)
    # jika pilih 2 akan lanjut ke fungsi proses sorting descending
    elif pilih == 2:
        proses_sorting_desc(menu)
    else:
        print(Fore.RED + '\nPERINGATAN! MENU TIDAK ADA.' + Style.RESET_ALL)
        input("\nTekan Enter untuk Kembali ke Jenis Sorting\n")
        proses_sorting(menu)

# fungsi sorting ascending
def proses_sorting_asc(menu):
    # sorted(iterable, key=key, reverse=reverse) -> untuk sorting iterable object
    # iterable ->  objek yang dapat diiterasi untuk di-sort (list, dictionary, tuple, dll)
    # dari data_mobil.items() diambil key-nya, dimana key = lambda x: x[key][nama kolom] (nama kolom -> merk, tipe, dll)
    # lalu di sort ascending berdasarkan values dari hasil slicing pada key function
    sort_mobil = sorted(data_mobil.items(), key = lambda x: x[1][menu])
    values = [[key, *value.values()] for key, value in sort_mobil]
    print('\n== HASIL SORTING MOBIL ==\n')
    print_table(values)
    input("Tekan Enter untuk Kembali ke Sorting Mobil")
    sorting_mobil()

# fungsi sorting descending
def proses_sorting_desc(menu):
    # sorted(iterable, key=key, reverse=reverse) -> untuk sorting iterable object
    # iterable ->  objek yang dapat diiterasi untuk di-sort (list, dictionary, tuple, dll)
    # dari data_mobil.items() diambil key-nya, dimana key = lambda x: x[key][nama kolom] (nama kolom -> merk, tipe, dll)
    # lalu di sort descending dgn reverse = True berdasarkan values dari hasil slicing pada key function
    sort_mobil = sorted(data_mobil.items(), key = lambda x: x[1][menu], reverse=True)
    values = [[key, *value.values()] for key, value in sort_mobil]
    print('\n== HASIL SORTING MOBIL ==\n')
    print_table(values)
    input("Tekan Enter untuk Kembali ke Sorting Mobil")
    sorting_mobil()

# fungsi untuk mode pesewa (pemilik rental mobil)
def mode_pesewa():
    print('-'*15)
    print('| MODE PESEWA |')
    print('-'*15)
    print('''
    1. Tambah Data Mobil
    2. Perbarui Data Mobil
    3. Hapus Data Mobil
    4. Kembali ke Menu Utama\n''')
    menu = input('Pilih Menu : ')
    # pastikan inputan user berupa digit -> lalu str akan diconvert ke int
    if menu.isdigit() == True:
        menu = int(menu)
    else:
        print(Fore.RED + '\nPERINGATAN! MASUKKAN INPUT HANYA BERUPA ANGKA.' + Style.RESET_ALL)
        input("\nTekan Enter untuk Kembali ke Mode Pesewa")
        print()
        mode_pesewa()
    empty = {}
    # menu untuk tambah mobil baru
    if menu == 1:
        print()
        print('-'*35)
        print('| MODE PESEWA > TAMBAH DATA MOBIL |')
        print('-'*35)
        tambah_mobil()
    # menu untuk memperbarui mobil
    elif menu == 2:
        # kalau data empty / tidak ada data, akan ada warning sign bahwa data mobil kosong
        if data_mobil == empty:
            print(Fore.RED + '\nPERINGATAN! DATA MOBIL KOSONG. TIDAK BISA MEMPERBARUI DATA. SILAHKAN TAMBAH DATA MOBIL.' + Style.RESET_ALL)
            input("\nTekan Enter untuk Kembali ke Mode Pesewa\n")
            mode_pesewa()
        else:
            perbarui_mobil()
    # menu untuk menghapus mobil
    elif menu == 3:
        # kalau data empty / tidak ada data, akan ada warning sign bahwa data mobil kosong
        if data_mobil == empty:
            print(Fore.RED + '\nPERINGATAN! DATA MOBIL KOSONG. TIDAK BISA MENGHAPUS DATA. SILAHKAN TAMBAH DATA MOBIL.' + Style.RESET_ALL)
            input("\nTekan Enter untuk Kembali ke Mode Pesewa\n")
            mode_pesewa()
        else:
            hapus_mobil()
    # menu untuk kembali ke menu utama
    elif menu == 4:
        menu_utama()
    else:
        print(Fore.RED + '\nPERINGATAN! MENU TIDAK ADA.' + Style.RESET_ALL)
        input("\nTekan Enter untuk Kembali ke Mode Pesewa\n")
        mode_pesewa()

# fungsi untuk tambah mobil
def tambah_mobil():
    print('\n== SILAHKAN ISI DATA MOBIL BARU ==\n')
    kode = input('Masukkan Kode Mobil: ').title()
    # kondisi dmn kode yang diinput harus berawalan dr M dan dilanjutkan dengan angka
    if not kode.startswith('M') or kode[1:].isdigit() == False:
        print(Fore.RED + '\nPERINGATAN! KODE HARUS DIAWALI DENGAN HURUF "M" DAN DIAKHIRI DENGAN ANGKA.' + Style.RESET_ALL)
        tambah_mobil()
    else:
        # jika kode ada dalam list keys data mobil, akan ada peringatan mobil sudah ada, dan menampilkan data mobil kode tsb
        if kode in list(data_mobil.keys()):
            print(Fore.RED + '\nPERINGATAN! KODE MOBIL SUDAH ADA.\n' + Style.RESET_ALL)
            print('== DATA MOBIL ==\n')
            idx = list(data_mobil.keys()).index(kode) # ambil index kode mobil
            values = [[[key, *values.values()] for key, values in data_mobil.items()][idx]]
            print_table(values)
            # konfirmasi apakah user tetap akan tambah data mobil baru?
            konfirmasi_lanjut_tambah()
        # jika kode belum ada di data, maka user dapat input data mobil baru
        else:
            merk = input('Masukkan Merk Mobil : ').title()
            # khusus tipe di convert jd .lower agar suv dan mpv terbaca
            tipe = input('Masukkan Tipe Mobil : ').lower()
            # jika tipe yg dimasukan suv/mpv akan di convert jd .upper
            if tipe == 'suv' or tipe == 'mpv':
                tipe = tipe.upper()
            else:
                tipe = tipe.title()
            kapasitas = input('Masukkan Kapasitas Mobil (Orang) : ')
            # jika inputan yang dimasukan adalah digit, maka str akan di convert ke int
            if kapasitas.isdigit() == True:
                kapasitas = int(kapasitas)
            else:
                print(Fore.RED + '\nPERINGATAN! MASUKKAN INPUT HANYA BERUPA ANGKA.' + Style.RESET_ALL)
                tambah_mobil()
            transmisi = input('Masukkan Transmisi Mobil (Manual / Otomatis) : ').title()
            tahun = input('Masukkan Tahun Keluaran Mobil : ')
            # jika inputan yang dimasukan adalah digit, maka str akan di convert ke int
            if tahun.isdigit() == True:
                tahun = int(tahun)
            else:
                print(Fore.RED + '\nPERINGATAN! MASUKKAN INPUT HANYA BERUPA ANGKA.' + Style.RESET_ALL)
                tambah_mobil()
            jumlah = input('Masukkan Jumlah Mobil (Unit) : ')
            # jika inputan yang dimasukan adalah digit, maka str akan di convert ke int
            if jumlah.isdigit() == True:
                jumlah = int(jumlah)
            else:
                print(Fore.RED + '\nPERINGATAN! MASUKKAN INPUT HANYA BERUPA ANGKA.' + Style.RESET_ALL)
                tambah_mobil()
            jenis_sewa = input('Masukkan Jenis Penyewaan Mobil (Supir / Supir/Lepas Kuci) : ').title()
            harga = input('Masukkan Harga Sewa Mobil (12 Jam) : ')
            # jika inputan yang dimasukan adalah digit, maka str akan di convert ke int
            if harga.isdigit() == True:
                harga = int(harga)
            else:
                print(Fore.RED + '\nPERINGATAN! MASUKKAN INPUT HANYA BERUPA ANGKA.' + Style.RESET_ALL)
                tambah_mobil()
            # data mobil akan dijadikan dict in dict baru
            mobil_baru = {
                            kode : {
                                'Merk'            : merk,
                                'Tipe'            : tipe,
                                'Kapasitas'       : f'{kapasitas} Orang',
                                'Transmisi'       : transmisi,
                                'Tahun'           : int(tahun),
                                'Jumlah'          : f'{jumlah} Unit',
                                'Jenis Sewa'      : jenis_sewa,
                                'Harga'           : harga 
                            }
            }
            # data dict mobil_baru akan di print untuk melihat hasil data mobil sebelum konfirmasi
            print('\n== DATA MOBIL BARU ==\n')
            values = [[key, *values.values()] for key, values in mobil_baru.items()]
            print_table(values)
            # lanjut ke fungsi konfirmasi_tambah dgn membawa parameter mobil_baru
            konfirmasi_tambah(mobil_baru)

# fungsi konfirmasi lanjut tambah jika kode yg dimasukkan salah
def konfirmasi_lanjut_tambah():
    konfirmasi = input(Fore.YELLOW + '\nApakah Anda ingin melanjutkan penambahan data mobil? (ya/tidak): ' + Style.RESET_ALL).lower()
    # jika ya maka akan mengulang untuk mengisi form tambah data mobil
    if konfirmasi == 'ya':
        tambah_mobil()
    # jika tidak akan kembali ke mode pesewa
    elif konfirmasi == 'tidak':
        input("\nTekan Enter untuk Kembali ke Mode Pesewa")
        print()
        mode_pesewa()
    else:
        print(Fore.RED + '\nPERINGATAN! MASUKKAN INPUT HANYA YA/TIDAK.' + Style.RESET_ALL)
        konfirmasi_lanjut_tambah()

# fungsi konfirmasi tambah mobil baru -> masuk ke daftar mobil
def konfirmasi_tambah(mobil_baru):
    konfirmasi = input(Fore.YELLOW + '\nApakah Anda yakin ingin menambahkan data mobil? (ya/tidak): ' + Style.RESET_ALL).lower()
    # jika ya, maka dict data_mobil akan di update dengan data yg ada di mobil_baru
    if konfirmasi == 'ya':
        data_mobil.update(mobil_baru)
        print(Fore.GREEN + '\nSUKSES! ANDA BERHASIL MENAMBAHKAN DATA MOBIL.' + Style.RESET_ALL)
        input("\nTekan Enter untuk Kembali ke Mode Pesewa")
        print()
        mode_pesewa()
    # jika tidak, maka data tidak akan tersimpan
    elif konfirmasi == 'tidak':
        print(Fore.RED + '\nERROR! ANDA GAGAL MENAMBAHKAN DATA MOBIL.' + Style.RESET_ALL)
        input("\nTekan Enter untuk Kembali ke Mode Pesewa")
        print()
        mode_pesewa()
    else:
        print(Fore.RED + '\nPERINGATAN! MASUKKAN INPUT HANYA YA/TIDAK.' + Style.RESET_ALL)
        konfirmasi_tambah(mobil_baru)

# fungsi untuk menu perbarui mobil
def perbarui_mobil():
    print()
    print('-'*37)
    print('| MODE PESEWA > PERBARUI DATA MOBIL |')
    print('-'*37)
    print('''
    1. Perbarui Semua Kolom pada Data Mobil
    2. Perbarui Kolom Tertentu pada Data Mobil
    3. Kembali ke Mode Pesewa''')
    menu = input('\nPilih Menu : ')
    # pastikan inputan user berupa digit -> lalu str akan diconvert ke int
    if menu.isdigit() == True:
        menu = int(menu)
    else:
        print(Fore.RED + '\nPERINGATAN! MASUKKAN INPUT HANYA BERUPA ANGKA.' + Style.RESET_ALL)
        input('\nTekan Enter untuk Kembali ke Perbarui Data Mobil')
        perbarui_mobil()
    # menu untuk perbarui data di semua kolom
    if menu == 1:
        print()
        print('-'*51)
        print('| MODE PESEWA > PERBARUI DATA MOBIL > SEMUA KOLOM |')
        print('-'*51)
        perbarui_mobil_semua()
    # menu untuk perbarui data di kolom tertentu saja
    elif menu == 2:
        print()
        print('-'*54)
        print('| MODE PESEWA > PERBARUI DATA MOBIL > KOLOM TERTENTU |')
        print('-'*54)
        perbarui_mobil_tertentu()
    # menu untuk kembali ke mode pesewa
    elif menu == 3:
        print()
        mode_pesewa()
    else:
        print(Fore.RED + '\nPERINGATAN! MENU TIDAK ADA.' + Style.RESET_ALL)
        input("\nTekan Enter untuk Kembali ke Perbarui Data Mobil")
        print()
        perbarui_mobil()

# fungsi untuk perbarui data mobil di semua kolom sekaligus
def perbarui_mobil_semua():
    print('\n== FORM PERBARUI DATA MOBIL ==')
    kode = input('\nMasukkan Kode Mobil: ').title()
    # jika kode ada di list keys data_mobil
    if kode in list(data_mobil.keys()):
        print('\n== DATA MOBIL ==\n')
        # ambil index kode mobil -> M01 : Index 0
        idx = list(data_mobil.keys()).index(kode)
        # values diambil dari key dan values dari data_mobil
        # *values -> merk, tipe, kapasitas, dll, values() -> kita ambil values dari *values
        # untuk ekstrak key, values harus dgn for loop key, values in data_mobil.items() -> berdasarkan index kode diatas
        values = [[[key, *values.values()] for key, values in data_mobil.items()][idx]]
        # print table sesuai dengan values diatas (berdasarkan kode yg ditulis) -> untuk melihat data mobil sesuai kode
        print_table(values)
        print()
        # krn memperbarui semua data, maka masukan semua data seperti tambah baru
        merk_baru = input('Masukkan Merk Mobil Baru : ').title()
        tipe_baru = input('Masukkan Tipe Mobil Baru : ').lower()
        if tipe_baru == 'suv' or tipe_baru == 'mpv':
            tipe_baru = tipe_baru.upper()
        else:
            tipe_baru = tipe_baru.title()
        kapasitas_baru = input('Masukkan Kapasitas Mobil Baru (Orang) : ')
        if kapasitas_baru.isdigit() == True:
            kapasitas_baru = int(kapasitas_baru)
        else:
            print(Fore.RED + '\nPERINGATAN! MASUKKAN INPUT HANYA BERUPA ANGKA.' + Style.RESET_ALL)
            perbarui_mobil_semua()
        transmisi_baru = input('Masukkan Jenis Transmisi Mobil Baru : ').title()
        tahun_baru = input('Masukkan Tahun Keluaran Mobil Baru : ')
        if tahun_baru.isdigit() == True:
            tahun_baru = int(tahun_baru)
        else:
            print(Fore.RED + '\nPERINGATAN! MASUKKAN INPUT HANYA BERUPA ANGKA.' + Style.RESET_ALL)
            perbarui_mobil_semua()
        jumlah_baru = input('Masukkan Jumlah Mobil Baru (Unit) : ')
        if jumlah_baru.isdigit() == True:
            jumlah_baru = int(jumlah_baru)
        else:
            print(Fore.RED + '\nPERINGATAN! MASUKKAN INPUT HANYA BERUPA ANGKA.' + Style.RESET_ALL)
            perbarui_mobil_semua()
        sewa_baru = input('Masukkan Jens Sewa Mobil Baru (Supir / Supir/Lepas Kunci) : ').title()
        harga_baru = input('Masukkan Harga (12 Jam) Mobil Baru : ')
        if harga_baru.isdigit() == True:
            harga_baru = int(harga_baru)
        else:
            print(Fore.RED + '\nPERINGATAN! MASUKKAN INPUT HANYA BERUPA ANGKA.' + Style.RESET_ALL)
            perbarui_mobil_semua()
        # sama seperti tambah mobil, data mobil akan dijadikan dict in dict baru
        mobil_baru = {
                        kode : {
                            'Merk'            : merk_baru,
                            'Tipe'            : tipe_baru,
                            'Kapasitas'       : f'{kapasitas_baru} Orang',
                            'Transmisi'       : transmisi_baru,
                            'Tahun'           : tahun_baru,
                            'Jumlah'          : f'{jumlah_baru} Unit',
                            'Jenis Sewa'      : sewa_baru,
                            'Harga'           : harga_baru       
                        }
        }
        # data dict mobil_baru akan di print untuk melihat hasil data mobil sebelum konfirmasi
        print('\n== DATA MOBIL BARU ==\n')
        values = [[key, *values.values()] for key, values in mobil_baru.items()]
        print_table(values)
        # lanjut ke fungsi konfirmasi perbarui semua data mobil dgn membawa parameter mobil_baru
        konfirmasi_lanjut_perbarui(kode, merk_baru, tipe_baru, kapasitas_baru, transmisi_baru, tahun_baru, jumlah_baru, sewa_baru, harga_baru)
    else:
        print(Fore.RED + '\nPERINGATAN! TIDAK ADA KODE MOBIL TERSEBUT DALAM DATA.\n' + Style.RESET_ALL)
        # jika tidak ada kode dalam data, lanjut ke konfirmasi apakah user masih ingin mengubah data?
        konfirmasi_perbarui_all()

# fungsi untuk konfirmasi perbarui semua data mobil
def konfirmasi_lanjut_perbarui(kode, merk_baru, tipe_baru, kapasitas_baru, transmisi_baru, tahun_baru, jumlah_baru, sewa_baru, harga_baru):
    konfirmasi = input(Fore.YELLOW + '\nApakah Anda yakin ingin memperbarui data mobil? (ya/tidak): ' + Style.RESET_ALL).lower()
    # jika ya, maka semua kolom akan diganti value-nya dengan value yang baru
    if konfirmasi == 'ya':
        data_mobil[kode]['Merk'] = merk_baru
        data_mobil[kode]['Tipe'] = tipe_baru
        data_mobil[kode]['Kapasitas'] = f'{kapasitas_baru} Orang'
        data_mobil[kode]['Transmisi'] = transmisi_baru
        data_mobil[kode]['Tahun'] = tahun_baru
        data_mobil[kode]['Jumlah'] = f'{jumlah_baru} Unit'
        data_mobil[kode]['Jenis Sewa'] = sewa_baru
        data_mobil[kode]['Harga'] = harga_baru
        print(Fore.GREEN + '\nSUKSES! ANDA BERHASIL MEMPERBARUI DATA MOBIL' + Style.RESET_ALL)
        input("\nTekan Enter untuk Kembali ke Perbarui Data Mobil")
        print()
        perbarui_mobil()
    # jika tidak, maka data baru mobil tidak tersimpan, dan masih terisi data yang lama
    elif konfirmasi == 'tidak':
        print(Fore.RED + '\nERROR! ANDA GAGAL MEMPERBARUI DATA MOBIL.' + Style.RESET_ALL)
        input("\nTekan Enter untuk Kembali ke Perbarui Data Mobil")
        print()
        perbarui_mobil()
    else:
        print(Fore.RED + '\nPERINGATAN! MASUKKAN INPUT HANYA YA/TIDAK.' + Style.RESET_ALL)
        konfirmasi_lanjut_perbarui(kode, merk_baru, tipe_baru, kapasitas_baru, transmisi_baru, tahun_baru, jumlah_baru, sewa_baru, harga_baru)

# fungsi untuk konfirmasi apakah user masih ingin mengubah data setelah salah input kode - khusus perbarui semua
def konfirmasi_perbarui_all():
    konfirmasi = input(Fore.YELLOW + 'Apakah Anda ingin melanjutkan memperbarui semua kolom pada data? (ya/tidak): ' + Style.RESET_ALL).lower()
    # jika ya, maka akan kembali ke form perbarui data mobil
    if konfirmasi == 'ya':
        perbarui_mobil_semua()
    # jika tidak, maka akan kembali ke perbarui data mobil
    elif konfirmasi == 'tidak':
        input("\nTekan Enter untuk Kembali ke Perbarui Data Mobil")
        print()
        perbarui_mobil()
    else:
        print(Fore.RED + '\nPERINGATAN! MASUKKAN INPUT HANYA YA/TIDAK.' + Style.RESET_ALL)
        konfirmasi_perbarui_all()

# fungsi untuk perbarui data mobil tertentu sesuai kode
def perbarui_mobil_tertentu():
    kode = input('\nMasukkan Kode Mobil: ').title()
    # jika kode ada di list keys data_mobil
    if kode in list(data_mobil.keys()):
        print('\n== DATA MOBIL ==\n')
        # ambil index kode mobil -> M01 : Index 0
        idx = list(data_mobil.keys()).index(kode)
        # values diambil dari key dan values dari data_mobil
        # *values -> merk, tipe, kapasitas, dll, values() -> kita ambil values dari *values
        # untuk ekstrak key, values harus dgn for loop key, values in data_mobil.items() -> berdasarkan index kode diatas
        values = [[[key, *values.values()] for key, values in data_mobil.items()][idx]]
        print_table(values)
        # masukan nama kolom yang ingin diperbarui datanya
        menu = input('\nMasukkan nama kolom pada data mobil yang datanya ingin diperbarui : ').title()
        # kolom yang diinput tidak boleh kode, krn kode adalah primary key
        if menu == 'Kode':
            print(Fore.RED + '\nPERINGATAN! KODE ADALAH' + '\x1B[3m' + ' PRIMARY KEY. ' '\x1B[0m' + Fore.RED + 'KODE TIDAK DAPAT DIPERBARUI.\n' + Style.RESET_ALL)
            konfirmasi_kode()
        elif menu == 'Merk':
            kolom = input('\nMasukkan Merk Mobil Baru: ').title()
            konfirmasi_perbarui_tertentu(kode, menu, kolom)
        elif menu == 'Tipe':
            kolom = input('\nMasukkan Tipe Mobil Baru: ').lower()
            if kolom == 'suv' or kolom == 'mpv':
                kolom = kolom.upper()
            else:
                kolom = kolom.title()
            konfirmasi_perbarui_tertentu(kode, menu, kolom)
        elif menu == 'Kapasitas':
            kolom = input('\nMasukkan Kapasitas Mobil Baru: ')
            if kolom.isdigit() == True:
                kolom = int(kolom)
            else:
                print(Fore.RED + '\nPERINGATAN! MASUKKAN INPUT HANYA BERUPA ANGKA.' + Style.RESET_ALL)
                perbarui_mobil_tertentu()
            konfirmasi_perbarui_tertentu(kode, menu, kolom)
        elif menu == 'Transmisi':
            kolom = input('\nMasukkan Jenis Transmisi Mobil Baru: ').title()
            konfirmasi_perbarui_tertentu(kode, menu, kolom)
        elif menu == 'Tahun':
            kolom = input('\nMasukkan Tahun Keluaran Mobil Baru: ')
            if kolom.isdigit() == True:
                kolom = int(kolom)
            else:
                print(Fore.RED + '\nPERINGATAN! MASUKKAN INPUT HANYA BERUPA ANGKA.' + Style.RESET_ALL)
                perbarui_mobil_tertentu()
            konfirmasi_perbarui_tertentu(kode, menu, kolom)
        elif menu == 'Jumlah':
            kolom = input('\nMasukkan Jumlah Unit Mobil Baru: ')
            if kolom.isdigit() == True:
                kolom = int(kolom)
            else:
                print(Fore.RED + '\nPERINGATAN! MASUKKAN INPUT HANYA BERUPA ANGKA.' + Style.RESET_ALL)
                perbarui_mobil_tertentu()
            konfirmasi_perbarui_tertentu(kode, menu, kolom)
        elif menu == 'Jenis Sewa':
            kolom = input('\nMasukkan Jenis Sewa Mobil Baru: ').title()
            konfirmasi_perbarui_tertentu(kode, menu, kolom)
        elif menu == 'Harga':
            kolom = input('\nMasukkan Harga (12 Jam) Mobil Baru: ')
            if kolom.isdigit() == True:
                kolom = int(kolom)
            else:
                print(Fore.RED + '\nPERINGATAN! MASUKKAN INPUT HANYA BERUPA ANGKA.' + Style.RESET_ALL)
                perbarui_mobil_tertentu()
            konfirmasi_perbarui_tertentu(kode, menu, kolom)
        else:
            print(Fore.RED + '\nPERINGATAN! TIDAK ADA JENIS KOLOM TERSEBUT PADA DATA MOBIL.' + Style.RESET_ALL)
            perbarui_mobil_tertentu()
    else:
        print(Fore.RED + '\nPERINGATAN! TIDAK ADA KODE MOBIL TERSEBUT DALAM DATA.\n' + Style.RESET_ALL)
        konfirmasi_kode()

# fungsi untuk konfirmasi apakah user masih ingin mengubah data setelah salah input kode - khusus perbarui tertentu
def konfirmasi_kode():
    konfirmasi = input(Fore.YELLOW + 'Apakah Anda ingin melanjutkan memperbarui data tertentu? (ya/tidak): ' + Style.RESET_ALL).lower()
    # jika ya, maka akan lanjut ke fungsi perbarui data mobil tertentu
    if konfirmasi == 'ya':
        perbarui_mobil_tertentu()
    # jika tidak, maka akan kembali ke perbarui data mobil
    elif konfirmasi == 'tidak':
        input("\nTekan Enter untuk Kembali ke Perbarui Data Mobil")
        print()
        perbarui_mobil() 
    else:
        print(Fore.RED + '\nPERINGATAN! MASUKKAN INPUT HANYA YA/TIDAK.' + Style.RESET_ALL)
        konfirmasi_kode()  

# fungsi untuk konfirmasi perbarui data mobil tertentu
def konfirmasi_perbarui_tertentu(kode, menu, kolom):
    konfirmasi = input(Fore.YELLOW + '\nApakah Anda ingin memperbarui data Merk? (ya/tidak): ' + Style.RESET_ALL).lower()
    # jika ya, maka value dr kolom tersebut akan diganti dengan value baru
    if konfirmasi == 'ya':
        data_mobil[kode][f'{menu}'] = kolom
        print(Fore.GREEN + '\nSUKSES! ANDA BERHASIL MEMPERBARUI DATA MOBIL' + Style.RESET_ALL)
        print('\n== DATA MOBIL BARU ==\n')
        idx = list(data_mobil.keys()).index(kode)
        values = [[[key, *values.values()] for key, values in data_mobil.items()][idx]]
        print(tabulate(values, headers=headers, tablefmt="pretty"))
        input("\nTekan Enter untuk Kembali ke Perbarui Data Mobil")
        print()
        perbarui_mobil()
    # jika tidak, maka value pada kolom tidak akan ter-update
    elif konfirmasi == 'tidak':
        print(Fore.RED + '\nERROR! ANDA GAGAL MEMPERBARUI DATA MOBIL.' + Style.RESET_ALL)
        input("\nTekan Enter untuk Kembali ke Perbarui Data Mobil")
        print()
        perbarui_mobil()
    else:
        print(Fore.RED + '\nPERINGATAN! MASUKKAN INPUT HANYA YA/TIDAK.' + Style.RESET_ALL)
        konfirmasi_perbarui_tertentu(kode, menu, kolom)

# fungsi untuk menu hapus mobil
def hapus_mobil():
    print()
    print('-'*34)
    print('| MODE PESEWA > HAPUS DATA MOBIL |')
    print('-'*34)
    print('''
    1. Hapus Semua Data Mobil
    2. Hapus Data Mobil Tertentu
    3. Kembali ke Mode Pesewa''')
    menu = input('\nPilih Menu : ')
    # pastikan inputan user berupa digit -> lalu str akan diconvert ke int
    if menu.isdigit() == True:
        menu = int(menu)
    else:
        print(Fore.RED + '\nPERINGATAN! MASUKKAN INPUT HANYA BERUPA ANGKA.' + Style.RESET_ALL)
        input("\nTekan Enter untuk Kembali ke Hapus Data Mobil")
        hapus_mobil()
    # menu untuk menghapus semua data mobil
    if menu == 1:
        print()
        print('-'*47)
        print('| MODE PESEWA > HAPUS DATA MOBIL > SEMUA DATA |')
        print('-'*47)
        hapus_mobil_semua()
    # menu untuk menghapus data mobil tertentu sesuai dengan kode yang dipilih
    elif menu == 2:
        print()
        print('-'*50)
        print('| MODE PESEWA > HAPUS DATA MOBIL > DATA TERTENTU |')
        print('-'*50)
        hapus_mobil_tertentu()
    elif menu == 3:
        print()
        mode_pesewa()
    else:
        print(Fore.RED + '\nPERINGATAN! MENU TIDAK ADA.' + Style.RESET_ALL)
        input("\nTekan Enter untuk Kembali ke Hapus Data Mobil")
        hapus_mobil()

# fungsi untuk menghapus semua data mobil
def hapus_mobil_semua():
    konfirmasi = input(Fore.YELLOW + '\nApakah Anda yakin ingin menghapus semua data mobil? (ya/tidak): ' + Style.RESET_ALL).lower()
    # jika ya, maka data mobil akan terhapus semua dgn menggunakan data_mobil.clear
    # dan akan ada beberapa menu yang tidak bisa dijalankan krn tidak ada data
    if konfirmasi == 'ya':
        data_mobil.clear()
        print(Fore.GREEN + '\nSUKSES! ANDA BERHASIL MENGHAPUS SEMUA DATA MOBIL.' + Style.RESET_ALL)
        input("\nTekan Enter untuk Kembali ke Mode Pesewa")
        print()
        mode_pesewa()
    # jika tidak, maka data masih akan tetap seperti semula
    elif konfirmasi == 'tidak':
        print(Fore.RED + '\nERROR! ANDA GAGAL MENGHAPUS SEMUA DATA MOBIL.' + Style.RESET_ALL)  
        input("\nTekan Enter untuk Kembali ke Hapus Data Mobil")
        print()
        hapus_mobil()   
    else:
        print(Fore.RED + '\nPERINGATAN! MASUKKAN INPUT HANYA YA/TIDAK.' + Style.RESET_ALL)  
        hapus_mobil_semua()

# fungsi untuk menghapus data mobil tertentu sesuai dengan kode yang dipilih
def hapus_mobil_tertentu():
    print()
    # tampilkan semua data mobil
    print('== DAFTAR MOBIL ==\n')
    values = [[key, *values.values()] for key, values in data_mobil.items()]
    print_table(values)
    # masukkan kode mobil yang ingin di hapus
    kode = input('Masukkan Kode Mobil yang akan Dihapus: ').title()
    # jika kode ada pada list keys di data_mobil
    if kode in list(data_mobil.keys()):
        # tampilkan datanya
        print('\n== DATA MOBIL ==\n')
        idx = list(data_mobil.keys()).index(kode)
        values = [[[key, *values.values()] for key, values in data_mobil.items()][idx]]
        print_table(values)
        # lanjut ke konfirmasi hapus data tsb
        konfirmasi_hapus(kode)  
    else:
        print(Fore.RED + '\nPERINGATAN! TIDAK ADA KODE MOBIL TERSEBUT DALAM DATA.\n' + Style.RESET_ALL)
        input("Tekan Enter untuk Kembali ke Hapus Data Mobil")
        hapus_mobil()

# fungsi untuk konfirmasi hapus data sesuai kode
def konfirmasi_hapus(kode):
    konfirmasi = input(Fore.YELLOW + '\nApakah Anda yakin ingin menghapus data mobil? (ya/tidak): ' + Style.RESET_ALL).lower()
    # jika ya, maka data akan dihapus menggunakan del data_mobil[kode] untuk menghapus sesuai dengan kode
    if konfirmasi == 'ya':
        print(Fore.GREEN + f'\nSUKSES! ANDA BERHASIL MENGHAPUS DATA MOBIL {(data_mobil[kode]["Merk"]).upper()}.' + Style.RESET_ALL)
        del data_mobil[kode]
        input("\nTekan Enter untuk Kembali ke Hapus Data Mobil")
        print()
        hapus_mobil()
    # jika tidak, maka data masih akan tetap seperti semula
    elif konfirmasi == 'tidak':
        print(Fore.RED + f'\nERROR! ANDA GAGAL MENGHAPUS DATA MOBIL KODE {kode}.' + Style.RESET_ALL)  
        input("\nTekan Enter untuk Kembali ke Hapus Data Mobil")
        print()
        hapus_mobil() 
    else:
        print(Fore.RED + '\nPERINGATAN! MASUKKAN INPUT HANYA YA/TIDAK.' + Style.RESET_ALL)  
        konfirmasi_hapus(kode)

# fungsi untuk menu mode penyewa
def mode_penyewa():
    print()
    print('-'*16)
    print('| MODE PENYEWA |')
    print('-'*16)
    print('''
    1. Sewa Mobil 
    2. Kembali ke Menu Utama\n''')
    menu = input('Pilih Menu : ')
    # pastikan inputan user berupa digit -> lalu str akan diconvert ke int
    if menu.isdigit() == True:
        menu = int(menu)
    else:
        print(Fore.RED + '\nPERINGATAN! MASUKKAN INPUT HANYA BERUPA ANGKA.' + Style.RESET_ALL)
        input("\nTekan Enter untuk Kembali ke Mode Penyewa")
        mode_penyewa()
    empty = {}
    # menu untuk menyewa mobil
    if menu == 1:
        # kalau data empty / tidak ada data, akan ada warning sign bahwa data mobil kosong
        if data_mobil == empty:
            print(Fore.RED + '\nPERINGATAN! DATA MOBIL KOSONG. TIDAK BISA SEWA MOBIL.' + Style.RESET_ALL)
            input("\nTekan Enter untuk Kembali ke Mode Penyewa\n")
            mode_penyewa()
        else:
            print()
            print('-'*29)
            print('| MODE PENYEWA > SEWA MOBIL |')
            print('-'*29)
            sewa_mobil()
    # menu untuk kembali ke menu utama
    elif menu == 2:
        menu_utama()
    else:
        print(Fore.RED + '\nPERINGATAN! MENU TIDAK ADA.' + Style.RESET_ALL)
        input("\nTekan Enter untuk Kembali ke Mode Penyewa")
        mode_penyewa()

# fungsi untuk menyewa mobil
def sewa_mobil():
    # pilih kode mobil yang ingin disewa
    kode = input('\nPilih Kode Mobil yang Ingin Disewa : ').title()
    # kode harus berawalan M dan dilanjutkan dengan angka
    if not kode.startswith('M') or kode[1:].isdigit() == False:
        print(Fore.RED + '\nPERINGATAN! KODE HARUS DIAWALI DENGAN HURUF "M" DAN DIAKHIRI DENGAN ANGKA.' + Style.RESET_ALL)
        sewa_mobil()
    else:
        # jika kode ada dalam list keys pada data_mobil
        if kode in list(data_mobil.keys()):
            # print data tersebut
            print('\n== DATA MOBIL ==\n')
            idx = list(data_mobil.keys()).index(kode)
            values = [[[key, *values.values()] for key, values in data_mobil.items()][idx]]
            print_table(values)
            print()
            # masukkan jumlah unit yang akan disewa
            jumlah = input('Masukkan Jumlah Unit Sewa : ')
            # pastikan inputan user berupa digit -> lalu str akan diconvert ke int
            if jumlah.isdigit() == True:
                jumlah = int(jumlah)
            else:
                print(Fore.RED + '\nPERINGATAN! MASUKKAN INPUT HANYA BERUPA ANGKA.' + Style.RESET_ALL)
                input("\nTekan Enter untuk Kembali ke Sewa Mobil")
                sewa_mobil()
            # jika jumlah unit yang dimasukkan kurang dari jumlah yang ada (masih ada stock)
            if jumlah <= int(data_mobil[kode]['Jumlah'].split()[0]):
                hari = input('Masukkan Jumlah Hari Sewa (12 Jam / Hari) : ')
                # lanjut ke input hari peminjaman/sewa
                # pastikan inputan user berupa digit -> lalu str akan diconvert ke int
                if hari.isdigit() == True:
                    hari = int(hari)
                else:
                    print(Fore.RED + '\nPERINGATAN! MASUKKAN INPUT HANYA BERUPA ANGKA.' + Style.RESET_ALL)
                    input("\nTekan Enter untuk Kembali ke Sewa Mobil")
                    sewa_mobil()
                # jika jenis sewa pada kode yg diinput merupakan jenis sewa yang bisa supir/lepas kunci
                if data_mobil[kode]['Jenis Sewa'] == 'Supir/Lepas Kunci':
                    jenis_sewa = input('Masukkan Jenis Sewa Mobil (Supir / Lepas Kunci) : ').title()
                    # maka user akan diberikan 1 inputan lagi untuk mengisi preferensi (supir/lepas kunci)
                    if jenis_sewa == 'Supir' or jenis_sewa == 'Lepas Kunci':
                        konfirmasi_sewa_lk(jenis_sewa, kode, hari, jumlah)
                    else:
                        print(Fore.RED + '\nPERINGATAN! MASUKKAN INPUT HANYA BERUPA SUPIR ATAU LEPAS KUNCI.' + Style.RESET_ALL)
                        input("\nTekan Enter untuk Kembali ke Sewa Mobil")
                        sewa_mobil()
                # jika jenis sewa pada kode yg diinput merupakan jenis sewa yang hanya bisa dengan supir, maka langsung lanjut ke konfirmasi
                else:
                    konfirmasi_sewa_s(kode, hari, jumlah)
            else:
                print(Fore.RED + '\nPERINGATAN! JUMLAH UNIT TIDAK MENCUKUPI.' + Style.RESET_ALL)
                input("\nTekan Enter untuk Kembali ke Sewa Mobil")
                sewa_mobil()
        else:
            print(Fore.RED + '\nPERINGATAN! TIDAK ADA KODE MOBIL TERSEBUT DALAM DATA.' + Style.RESET_ALL)
            sewa_mobil()

# fungsi konfirmasi sewa jika jenis sewa supir/lepas kunci
def konfirmasi_sewa_lk(jenis_sewa, kode, hari, jumlah):
    konfirmasi = input(Fore.YELLOW + '\nApakah Anda ingin melanjutkan pesanan? (ya/tidak): ' + Style.RESET_ALL).lower()
    # jika ya, maka akan lanjut print invoice
    if konfirmasi == 'ya':
        print(Fore.GREEN + '\nSUKSES! ANDA BERHASIL MEMESAN MOBIL. BERIKUT INVOICE ANDA.' + Style.RESET_ALL)
        invoice_lk(jenis_sewa, kode, hari, jumlah)
        # data pada kolom jumlah (unit) akan dikurangi sesuai jumlah yang dipesan
        x = int(data_mobil[kode]['Jumlah'].split()[0]) - jumlah
        # ubah data pada kolom jumlah sesuai dengan hasil diatas
        data_mobil[kode]['Jumlah'] = f'{x} Unit'
    # jika tidak, maka tidak akan ada transaksi, dan data jumlah tidak akan berubah
    elif konfirmasi == 'tidak':
        print(Fore.RED + '\nERROR! ANDA GAGAL MEMESAN MOBIL.' + Style.RESET_ALL)
    else:
        print(Fore.RED + '\nPERINGATAN! MASUKKAN INPUT HANYA YA/TIDAK.' + Style.RESET_ALL)
        konfirmasi_sewa_lk(jenis_sewa, kode, hari, jumlah)

# fungsi invoice sewa jika jenis sewa supir/lepas kunci
def invoice_lk(jenis_sewa, kode, hari, jumlah):
    print('\n== INVOICE ==\n')
    # jika jenis sewa yg dipilih supir, akan otomatis ada transaksi memesan supir pada invoice
    if jenis_sewa == 'Supir':
        # total mobil adalah total pembayaran pemesanan mobil
        total_mobil = jumlah * hari * data_mobil[kode]['Harga']
        # total supir adalah total pembayaran pemesanan supir
        total_supir = jumlah * hari * 150000
        # total all adalah total dari 2 variable diatas
        total_all_s = total_mobil + total_supir
        headers = ['Nama Barang', 'Jumlah', 'Hari (12 Jam)', 'Harga', 'Total']
        # masukkan kedalam dict baru
        inv = {
                'Mobil' : {
                    'Nama Barang'    : data_mobil[kode]['Merk'],
                    'Jumlah'        : jumlah,
                    'Hari (12 Jam)' : hari,
                    'Harga'         : data_mobil[kode]['Harga'],
                    'Total'         : total_mobil
                },
                
                'Supir' : {
                    'Nama Barang'   : 'Supir',
                    'Jumlah'        : jumlah,
                    'Hari (12 Jam)' : hari,
                    'Harga'         : 150000,
                    'Total'         : total_supir
                }
            }
        # values diambil dari key dan values dari inv
        # *values -> Nama Barang, Jumlah, dll, values() -> kita ambil values dari *values
        # untuk ekstrak key, values harus dgn for loop key, values in inv.items()
        values = [[*values.values()] for key, values in inv.items()]
        print(tabulate(values, headers=headers, tablefmt="pretty"))
        print('-'*61)
        print(f'Total Pembayaran (Dengan Supir) = {total_all_s}')
        print('-'*61)
        print('Pembayaran\nBank BCA a/n CV Bandung Rental Mobil\nNo. Rekening: 3123456')
        print('-'*61)
        print('\n== TERIMA KASIH! ==')
    # jika jenis sewa yg dipilih lepas kunci, maka invoice hanya berisi total harga mobil saja
    else:
        total_mobil = jumlah * hari * data_mobil[kode]['Harga']
        headers = ['Nama Barang', 'Jumlah', 'Hari (12 Jam)', 'Harga', 'Total']
        inv = {
                'Mobil' : {
                    'Nama Barang'   : data_mobil[kode]['Merk'],
                    'Jumlah'        : jumlah,
                    'Hari (12 Jam)' : hari,
                    'Harga'         : data_mobil[kode]['Harga'],
                    'Total'         : total_mobil
                }
            }
        values = [[*values.values()] for key, values in inv.items()]
        print(tabulate(values, headers=headers, tablefmt="pretty"))
        print('-'*61)
        print(f'Total Pembayaran (Lepas Kunci) = {total_mobil}')
        print('-'*61)
        print('Pembayaran\nBank BCA a/n CV Bandung Rental Mobil\nNo. Rekening: 3123456')
        print('-'*61)
        print('\n== TERIMA KASIH! ==\n')
        input("\nTekan Enter untuk Kembali ke Menu Utama")
        menu_utama()

# fungsi konfirmasi sewa jika jenis sewa hanya bisa supir
def konfirmasi_sewa_s(kode, hari, jumlah):
    konfirmasi = input(Fore.YELLOW + '\nApakah Anda ingin melanjutkan pesanan? (ya/tidak): ' + Style.RESET_ALL).lower()
     # jika ya, maka akan lanjut print invoice
    if konfirmasi == 'ya':
        print(Fore.GREEN + '\nSUKSES! ANDA BERHASIL MEMESAN MOBIL. BERIKUT INVOICE ANDA.' + Style.RESET_ALL)
        invoice_s(kode, hari, jumlah)
        # data pada kolom jumlah (unit) akan dikurangi sesuai jumlah yang dipesan
        x = int(data_mobil[kode]['Jumlah'].split()[0]) - jumlah
        # ubah data pada kolom jumlah sesuai dengan hasil diatas
        data_mobil[kode]['Jumlah'] = f'{x} Unit'
        input("\nTekan Enter untuk Kembali ke Menu Utama")
        menu_utama()
    # jika tidak, maka tidak akan ada transaksi, dan data jumlah tidak akan berubah
    elif konfirmasi == 'tidak':
        print(Fore.RED + '\nERROR! ANDA GAGAL MEMESAN MOBIL.' + Style.RESET_ALL)
    else:
        print(Fore.RED + '\nPERINGATAN! MASUKKAN INPUT HANYA YA/TIDAK.' + Style.RESET_ALL)
        konfirmasi_sewa_s(kode, hari, jumlah)

# fungsi invoice sewa jika jenis sewa hanya bisa supir
def invoice_s(kode, hari, jumlah):
    # karena pilihan jenis sewa hanya supir, maka otomatis ada transaksi memesan supir pada invoice
    print('\n== INVOICE ==\n')
    total_mobil = jumlah * hari * data_mobil[kode]['Harga']
    total_supir = jumlah * hari * 150000
    total_all_s = total_mobil + total_supir
    headers = ['Nama Barang', 'Jumlah', 'Hari (12 Jam)', 'Harga', 'Total']
    inv = {
                'Mobil' : {
                    'Nama Barang'    : data_mobil[kode]['Merk'],
                    'Jumlah'        : jumlah,
                    'Hari (12 Jam)' : hari,
                    'Harga'         : data_mobil[kode]['Harga'],
                    'Total'         : total_mobil
                },
                
                'Supir' : {
                    'Nama Barang'   : 'Supir',
                    'Jumlah'        : jumlah,
                    'Hari (12 Jam)' : hari,
                    'Harga'         : 150000,
                    'Total'         : total_supir
                }
            }
    values = [[*values.values()] for key, values in inv.items()]
    print(tabulate(values, headers=headers, tablefmt="pretty"))
    print('-'*61)
    print(f'Total Pembayaran (Dengan Supir) = {total_all_s}')
    print('-'*61)
    print('Pembayaran\nBank BCA a/n CV Bandung Rental Mobil\nNo. Rekening: 3123456')
    print('-'*61)
    print('\n== TERIMA KASIH! ==')

# fungsi untuk print tabel data mobil
def print_table(values):
    print(tabulate(values, headers=headers, tablefmt="pretty"))
    print('\n*** Catatan: Harga diatas adalah harga sewa mobil saja. Supir tambah 150000 / 12 Jam.\n')

# JALANKAN PROGRAM
menu_utama()