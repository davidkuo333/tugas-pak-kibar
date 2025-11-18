print("Selamat datang di cerita horror interaktif!")
print("Kamu berjalan sendirian di hutan gelap, hanya ditemani suara angin dan ranting yang patah.")
print("Tiba-tiba, kamu mendengar suara aneh di kejauhan.")
print("Apa yang akan kamu lakukan?")
print("1. Mendekati suara itu")
print("2. Berlari menjauh secepat mungkin")
print("3. Berhenti dan mencoba bersembunyi")

pilihan1 = input("Masukkan pilihanmu (1/2/3): ")

if pilihan1 == "1":
    print("\nKamu mendekati suara itu dengan hati-hati...")
    print("Di depanmu, kamu melihat sebuah rumah tua yang tampak kosong.")
    print("Apa yang akan kamu lakukan?")
    print("1. Masuk ke rumah")
    print("2. Mengintip dari jendela")
    print("3. Menghindar dan kembali ke hutan")

    pilihan2 = input("Masukkan pilihanmu (1/2/3): ")

    if pilihan2 == "1":
        print("\nKamu membuka pintu dan masuk...")
        print("Lampu tiba-tiba menyala sendiri dan kamu melihat bayangan hitam berdiri di sudut ruangan!")
        print("Kamu mencoba berlari, tapi pintu tertutup sendiri dan bayangan itu mendekat...")
        print("Tangan dingin menepuk bahumu. Semua menjadi gelap. Game over.")
    elif pilihan2 == "2":
        print("\nKamu mengintip dari jendela...")
        print("Bayangan itu menoleh tepat ke arahmu. Kamu ketakutan dan berlari mundur...")
        print("Namun, ranting pohon menamparmu dan kamu jatuh. Bayangan itu mendekat...")
        print("Kamu merasakan napas dingin di lehermu. Game over.")
    elif pilihan2 == "3":
        print("\nKamu memutuskan untuk menghindar...")
        print("Saat berjalan menjauh, kamu tersesat di hutan yang semakin gelap...")
        print("Suara-suara aneh muncul dari sekelilingmu, dan bayangan mulai mengepungmu. Game over.")
    else:
        print("\nPilihan tidak valid. Tiba-tiba, tanah di bawahmu runtuh dan kamu jatuh ke kegelapan. Game over.")

elif pilihan1 == "2":
    print("\nKamu berlari menjauh dari suara itu...")
    print("Tiba-tiba, kamu menemukan jalan setapak yang bercabang.")
    print("Pilih jalanmu:")
    print("1. Jalan ke kiri yang gelap dan lembap")
    print("2. Jalan ke kanan yang tampak lebih terang")
    print("3. Berbalik kembali ke hutan sebelumnya")

    pilihan2 = input("Masukkan pilihanmu (1/2/3): ")

    if pilihan2 == "1":
        print("\nKamu berjalan di jalan gelap...")
        print("Sesuatu menarik kakimu, dan kamu jatuh ke lubang yang dalam!")
        print("Di dasar lubang, ada bisikan yang mengerikan: 'Selamat datang di rumah baru mu.' Game over.")
    elif pilihan2 == "2":
        print("\nKamu berjalan di jalan yang tampak lebih terang...")
        print("Namun, pohon-pohon mulai menutup cahaya, dan bayangan muncul di sekelilingmu...")
        print("Kamu mencoba berlari, tapi kaki terasa berat, dan bayangan itu menangkapmu. Game over.")
    elif pilihan2 == "3":
        print("\nKamu kembali ke hutan sebelumnya...")
        print("Tapi suara itu lebih dekat sekarang. Sesuatu menyentuh bahumu dari belakang...")
        print("Kamu menjerit tapi tak ada yang mendengar. Game over.")
    else:
        print("\nPilihan tidak valid. Tiba-tiba, bayangan muncul dari semak-semak dan menyapamu dengan dingin. Game over.")

elif pilihan1 == "3":
    print("\nKamu bersembunyi di balik pohon...")
    print("Bayangan itu berjalan melewati tempatmu bersembunyi, tapi tiba-tiba berhenti tepat di belakangmu!")
    print("Apa yang akan kamu lakukan?")
    print("1. Lari secepat mungkin")
    print("2. Tetap diam dan berharap tidak terlihat")
    print("3. Memanggil bayangan itu dengan suara gemetar")

    pilihan2 = input("Masukkan pilihanmu (1/2/3): ")

    if pilihan2 == "1":
        print("\nKamu berlari secepat mungkin...")
        print("Namun, bayangan itu mengejarmu dan tiba-tiba menghilang di depanmu.")
        print("Kamu tersesat di hutan tanpa jalan keluar. Game over.")
    elif pilihan2 == "2":
        print("\nKamu tetap diam...")
        print("Bayangan itu mencondongkan kepala ke arahmu dan mendesis...")
        print("Tiba-tiba tangan dingin menyentuh wajahmu. Semua menjadi gelap. Game over.")
    elif pilihan2 == "3":
        print("\nKamu mencoba memanggilnya...")
        print("Bayangan itu berhenti, menatapmu dengan mata merah menyala...")
        print("Seketika, suara tertawa menyeramkan terdengar, dan kamu pingsan. Game over.")
    else:
        print("\nPilihan tidak valid. Bayangan itu mendekat dan menghilangkanmu dalam sekejap. Game over.")

else:
    print("\nPilihan tidak valid. Kegelapan menelanmu sebelum cerita dimulai. Game over.")
