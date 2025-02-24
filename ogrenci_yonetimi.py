ogrenciler = {}

def ogrenci_ekle():
    numara = input("Öğrenci numarası: ")
    if numara in ogrenciler:
        print("Bu numaraya sahip bir öğrenci zaten var!")
        return
    ad = input("Öğrenci adı: ")
    soyad = input("Öğrenci soyadı: ")
    bolum = input("Bölüm: ")
    not_ort = float(input("Not ortalaması: "))
    ogrenciler[numara] = {"ad": ad, "soyad": soyad, "bolum": bolum, "not_ort": not_ort}
    print("Öğrenci sisteme kayıt edildi!\n")

def ogrenci_listele():
    if not ogrenciler:
        print("Önce öğrenci ekleyiniz \n")
        return
    for numara, bilgiler in ogrenciler.items():
        print(f"Numara: {numara}, Ad: {bilgiler['ad']}, Soyad: {bilgiler['soyad']}, Bölüm: {bilgiler['bolum']}, Not Ort.: {bilgiler['not_ort']}")
    print()

def ogrenci_goruntule():
    numara = input("Bilgilerini görmek istediğiniz öğrenci numarası: ")
    if numara in ogrenciler:
        bilgiler = ogrenciler[numara]
        print(f"Ad: {bilgiler['ad']}, Soyad: {bilgiler['soyad']}, Bölüm: {bilgiler['bolum']}, Not Ort.: {bilgiler['not_ort']}\n")
    else:
        print("Öğrenci bulunamadı!\n")

def ogrenci_guncelle():
    numara = input("Bilgilerini güncellemek istediğiniz öğrenci numarası: ")
    if numara in ogrenciler:
        print("Güncel bilgileri giriniz (Boş bırakılanlar değişmeyecek)")
        ad = input("Yeni ad: ") or ogrenciler[numara]['ad']
        soyad = input("Yeni soyad: ") or ogrenciler[numara]['soyad']
        bolum = input("Yeni bölüm: ") or ogrenciler[numara]['bolum']
        not_ort = input("Yeni not ortalaması: ")
        not_ort = float(not_ort) if not_ort else ogrenciler[numara]['not_ort']
        ogrenciler[numara] = {"ad": ad, "soyad": soyad, "bolum": bolum, "not_ort": not_ort}
        print("Öğrenci bilgileri güncellendi!\n")
    else:
        print("Öğrenci bulunamadı!\n")

def ogrenci_sil():
    numara = input("Silmek istediğiniz öğrenci numarası: ")
    if numara in ogrenciler:
        del ogrenciler[numara]
        print("Öğrenci silindi!\n")
    else:
        print("Öğrenci bulunamadı!\n")

def menu():
    while True:
        print("\nÖĞRENCİ YÖNETİM SİSTEMİ")
        print("1. Öğrenci Ekle")
        print("2. Öğrencileri Listele")
        print("3. Belirli Bir Öğrenciyi Görüntüle")
        print("4. Öğrenci Bilgilerini Güncelle")
        print("5. Öğrenci Sil")
        print("6. Çıkış")
        secim = input("Seçiminizi yapın: ")
        if secim == "1":
            ogrenci_ekle()
        elif secim == "2":
            ogrenci_listele()
        elif secim == "3":
            ogrenci_goruntule()
        elif secim == "4":
            ogrenci_guncelle()
        elif secim == "5":
            ogrenci_sil()
        elif secim == "6":
            print("Çıkış yapılıyor.")
            break
        else:
            print("Geçersiz seçim, tekrar deneyin!\n")

menu()
