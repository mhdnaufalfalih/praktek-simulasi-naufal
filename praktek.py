print("=== PROGRAM KELULUSAN UJIAN MATEMATIKA ===")

nama = input("Masukkan Nama Mahasiswa: ")

if nama.lower() == "andi":
    target = 70
elif nama.lower() == "budi":
    target = 75
elif nama.lower () == "citra":
    target = 80
else:
    print("Nama mahasiswa tidak terdaftar!")
    target = 0

if target != 0:
    print("Nama:", nama)
    print("target nilai:", target)


    percobaan = 0
    nilai = 0

    while percobaan < 3 and nilai < target:
        nilai = int(input("Masukkan Nilai Ujian: "))
        percobaan += 1

        print("Percobaan ke-")
        if nilai >= target:
            print("nilai mencapai target!")
        else:
            print("Nilai belum mencapai target!.")
        if nilai >= target:
            print(nama, "berhasil lulus setelah",
            percobaan, "kali percobaan!")
        else:
            print(nama, "tidak lulus setelah 3 kali percobaan.")