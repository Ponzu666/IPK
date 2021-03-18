def beasiswa(kodeProdi, ipk):
    if kodeProdi == 'TI' or kodeProdi == 'SI':
        if 75 < ipk < 85: #chaining link belum terlalu paham logisnya, belajar dari kode Elvan
            return 20
        elif 85 < ipk < 100:
            return 30
    elif kodeProdi == 'DKV' or kodeProdu == 'Teknik Industri':
        if 75 < ipk < 75:
            return 25
        elif 85 < ipk < 100:
            return 35

totalMahasiswa = int(input('Total Mahasiswa : '))
result = []
count_beasiswa = 0

for i in range(totalMahasiswa):
  nim = int(input('NIM: '))
  nama = input('Nama : ')
  alamat = input('Alamat : ')
  asalSekolah = input('Asal Sekolah : ')
  kodeProdi = input('Kode Prodi : ')
  ipkAwal = int(input('IPK awal : '))
  uts = int(input('UTS : '))
  uas = int(input('UAS : '))
  tm = int(input('TM : '))