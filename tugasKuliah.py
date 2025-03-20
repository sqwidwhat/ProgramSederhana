class TugasKuliah:
    def hitungTotalBelanja(self):
        ttlBelanja = int(input("Masukkan total belanja: "))
        if ttlBelanja >= 150000:
            biaya = ttlBelanja - (ttlBelanja * 0.1)
        else:
            biaya = ttlBelanja
        print(f"Total yang harus dibayar: Rp{biaya:.2f}")

    def prediksiBilangan(self):
        bilangan = float(input("Masukan angka: "))
        if bilangan % 2 == 0:
            print(f"{bilangan} adalah bilangan genap")
        else:
            print(f"{bilangan} adalah bilangan ganjil")

    def membandingkanBilangan(self):
        bil1 = float(input("Masukan bilangan pertama: "))
        bil2 = float(input("Masukan bilagan kedua: "))

        if bil1 > bil2:
            print(f"{bil1} lebih besar dari {bil2}")
        elif bil2 > bil1:
            print(f"{bil2} lebih besar dari {bil1}")
        else:
            print(f"{bil1} sama besar {bil2}")

    def gajiKaryawan(self):
        golongan = input("Masukkan jenis golongan (A, B, C, D): ").strip().upper()

        if golongan == 'A':
            gaji = 2000000
        elif golongan == 'B':
            gaji = 1500000
        elif golongan == 'C':
            gaji = 1000000
        elif golongan == 'D':
            gaji = 800000
        else:
            print("Input golongan dengan benar!")
            return  # Keluar dari fungsi jika input salah

        print(f"Golongan {golongan} mendapatkan gaji sebesar Rp{gaji:,}")
        return gaji  # Mengembalikan nilai gaji jika diperlukan

    def gradeNilai(self):
        try:
            nilai = float(input("Masukkan nilai: "))
        except ValueError:
            print("Input harus berupa angka!")
            return

        if 80 <= nilai <= 100:
            grade = 'A'
        elif 70 <= nilai < 80:
            grade = 'B'
        elif 60 <= nilai < 70:
            grade = 'C'
        elif 40 <= nilai < 60:
            grade = 'D'
        elif 0 <= nilai < 40:
            grade = 'E'
        else:
            print("Input nilai di luar rentang 0-100!")
            return

        print(f"Nilai: {nilai}\nGrade: {grade}")

    def besarKecil(self):
        bill1 = float(input("Masukan bilangan pertama: "))
        bill2 = float(input("Masukan bilangan kedua: "))
        bill3 = float(input("Masukan bilangan ketiga: "))

        if bill1 == bill2 == bill3:
            print("Ketiga bilangan memiliki nilai yang sama.")
        elif bill1 >= bill2 and bill1 >= bill3:
            print(f"Bilangan terbesar adalah {bill1}")
        elif bill2 >= bill1 and bill2 >= bill3:
            print(f"Bilangan terbesar adalah {bill2}")
        else:
            print(f"Bilangan terbesar adalah {bill3}")

    def upahPerJam(self):
        nama = input("Masukan nama anda: ")
        golongan = input("Masukan golongan A, B, C dan D: ").strip().upper()
        jamKerja = float(input("Masukan jumlah jam kerja: "))
        tarif = {'A':4000, 'B':5000, 'C':6000, 'D':7500}

        if golongan not in tarif:
            print("Input golongan yang benar!")
            return

        jamLembur = max(0, jamKerja - 48)
        upahLembur = jamLembur * 3000

        jamNormal = min(48, jamKerja)
        upahPokok = jamNormal * tarif[golongan]

        totalGaji = upahPokok + upahLembur

        print(f"{nama} golongan {golongan} menerima gaji sebesar Rp.{totalGaji:,.2f}".replace(',', '.'))

    def hargaSaputangan(self):
        banyak = int(input("Masukan jumlah saputangan yang ingin dibeli: "))

        lusin = banyak // 12
        sisa= banyak % 12

        hargaLusin = lusin * 15000
        hargaSisa = sisa * 1500
        ttlHarga = hargaLusin + hargaSisa

        diskon = 0
        if (lusin >= 10) and (lusin <= 30):
            diskon = 0.1
        elif lusin > 30:
            diskon = 0.2

        ttlDiskon = ttlHarga * diskon
        hargaSetelahDiskon = ttlHarga - ttlDiskon
        print(f"Total harga: Rp{ttlHarga:,.2f}".replace(',', '.'))
        print(f"Diskon sebesar: Rp{ttlDiskon:,.2f}".replace(',', '.'))
        print(f"Total harga setelah diskon: Rp{hargaSetelahDiskon:,.2f}".replace(',', '.'))

    def temperatur(self):
        fahrenheit = float(input("Masukan suhu (Fahrenheit): "))
        celcius = 5 / 9 * (fahrenheit - 32)

        if celcius > 30:
            suhu = "Panas"
        elif celcius < 25:
            suhu = "Dingin"
        else:
            suhu = "Normal"

        print(f"{celcius:.2f}°C \nStatus {suhu}")

    def password(self):
        sandi = input("Masukan sandi: ")
        password = ["ANDIKA", "STMIK"]
        item = 2
        for i in range(item):
            if sandi in password:
                print("Sandi benar")
                break
            else:
                print("Password salah")
                sandi = input("Coba lagi: ")

def main():
    tugas = TugasKuliah()  # Membuat objek dari kelas TugasKuliah

    while True:
        print("\nMenu: ")
        print("1. Menghitung total belanja")
        print("2. Genap atau ganjil")
        print("3. Membadningkan Bilangan")
        print("4. Gaji karyawan")
        print("5. Grade Nilai")
        print("6. Bilangan terbesar")
        print("7. Upah per jam")
        print("8. Harga sapu tangan")
        print("9. Temperatur")
        print("10. Password")
        print("11. Keluar")

        pilihan = input("Masukkan pilihan: ")

        if pilihan == '1':
            tugas.hitungTotalBelanja()
        elif pilihan == '2':
            tugas.prediksiBilangan()
        elif pilihan == '3':
            tugas.membandingkanBilangan()
        elif pilihan == '4':
            tugas.gajiKaryawan()
        elif pilihan == '5':
            tugas.gradeNilai()
        elif pilihan == '6':
            tugas.besarKecil()
        elif pilihan == '7':
            tugas.upahPerJam()
        elif pilihan == '8':
            tugas.hargaSaputangan()
        elif pilihan == '9':
            tugas.temperatur()
        elif pilihan == '10':
            tugas.password()
        elif pilihan == '11':
            print("Terima kasih, program selesai.")
            break
        else:
            print("Pilihan tidak valid! Silakan coba lagi.")


if __name__ == "__main__":
    main()
