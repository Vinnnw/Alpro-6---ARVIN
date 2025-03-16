def hitung_ips():
    jumlah_mk = int(input("berapa jumlah mata kuliah? "))

    total_bobot = 0
    sks_per_mk = 3 

    for i in range(jumlah_mk):
        nilai = input(f"NIlai MK {i+1} : ")

        if nilai == "A" or nilai == "a":
            bobot = 4
        elif nilai == "B" or nilai == "b":
            bobot = 3
        elif nilai == "C" or nilai == "c":
            bobot = 2
        elif nilai == "D" or nilai == "d":
            bobot = 1
        else:
            print("Masukkan Hanya A, B, C, atau D")
            return

        total_bobot += bobot * sks_per_mk 

    total_sks = jumlah_mk * sks_per_mk
    ips = total_bobot / total_sks

    print(f"Nilai IPS anda semester ini: {ips:.2f}")

hitung_ips()
