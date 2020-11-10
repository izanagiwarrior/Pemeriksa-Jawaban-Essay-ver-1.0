print("===================================================")
print("========= Pemeriksa Jawaban Essay ver 1.0 =========")
print("===================================================")
print("                      Pengembang : M. Faiz Triputra\n")
jumlahSoal = int(input("Masukkan Jumlah Soal : "))
daftarJawaban = []
print("\n================== KUNCI JAWABAN ==================\n")
for i in range(jumlahSoal):
    running = True
    temp = []
    print("Masukkan Kunci Jawaban dari Soal ke - %d : , dan ketik 'd' jika selesai mengisi jawaban" %(i+1))
    while running:
        kunciJawaban = input()
        if kunciJawaban == "d" :
            running = False
        else:
            temp.append(kunciJawaban)
    temp2 = " ".join(temp)
    daftarJawaban.append(temp2)
Running = True
while Running:
    print("\n================== JAWABAN SISWA ==================\n")
    print("""Pada program ini anda bisa copy paste jawaban siswa dengan menurun ataupun di input 1 per 1
    \n""")
    Benar = 0
    for i in range(jumlahSoal):
        tempSplit = daftarJawaban[i].split()
        tempKunci = set(tempSplit)
        running = True
        temp = []
        temp3 = []
        nilaiTemp = 0
        print("Masukkan Kunci Jawaban dari Soal ke - %d : , dan ketik 'd' jika selesai mengisi jawaban" %(i+1))
        while running:
            siswaJawaban = input()
            if siswaJawaban == "d" :
                running = False
            else:
                temp.append(siswaJawaban)
        temp2 = " ".join(temp)
        temp3.append(temp2)
        tempJawaban = temp3[0].split()
        tempJawaban = set(tempJawaban)
        temp4 = tempJawaban.intersection(tempKunci)
        nilaiTemp = len(temp4)
        nilaiKunci = len(tempKunci)
        print("\nJawaban Siswa memiliki ketepatan",nilaiTemp,"dari",nilaiKunci,".")
        nilaiAkhir = (nilaiTemp/len(tempKunci))/jumlahSoal
        Benar += nilaiAkhir
    print("Nilai :",round(float((Benar/len(daftarJawaban))*100),2))
    Enter = input("\nIngin memeriksa siswa selanjutnya? # Cukup Menekan tombol Enter untuk lanjut, dan ketik 'Exit' untuk keluar dari aplikasi.\n")
    if Enter:
        Running = False

# 082189100482 => Kalau kamu mengerti codingan ini dan mau mengembangkan bersama. Terima Kasih.