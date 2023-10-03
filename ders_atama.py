import tkinter as tk
from tkinter import simpledialog

class Yemek:
    def __init__(self, baslik, icerik, tarih):
        self.baslik = baslik
        self.icerik = icerik
        self.tarih = tarih

class Musteri:
    def __init__(self, adi, soyadi, musteri_no):
        self.adi = adi
        self.soyadi = soyadi
        self.musteri_no = musteri_no
        self.yemekler = []

    def musteri_bilgileri(self):
        return f"Müsteri Adı: {self.adi}\nMüsteri Soyadı: {self.soyadi}\nMüsteri No: {self.musteri_no}"

    def yemek_ekle(self, Yemek):
        self.yemekler.append(Yemek)

class Uygulama(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Müsteri Siparis Atama Sistemi")
        self.geometry("400x400")

        self.musteri_listesi = []
        self.yemek_listesi = []

        self.liste_musteri = tk.Listbox(self, selectmode=tk.SINGLE)
        self.liste_musteri.pack(pady=10)

        self.liste_yemek = tk.Listbox(self, selectmode=tk.SINGLE)
        self.liste_yemek.pack(pady=10)

        self.atama_btn = tk.Button(self, text="Yemek Ata", command=self.yemek_ata)
        self.atama_btn.pack()

    def yeni_musteri_ekle(self):
        adi = simpledialog.askstring("Yeni Müsteri Ekle", "Müsteri Adı:")
        soyadi = simpledialog.askstring("Yeni Müsteri Ekle", "Müsteri Soyadı:")
        musteri_no = simpledialog.askstring("Yeni Müsteri Ekle", "Müsteri No:")

        if adi and soyadi and musteri_no:
            yeni_musteri = Musteri(adi, soyadi, musteri_no)
            self.musteri_listesi.append(yeni_musteri)
            self.liste_musteri.insert(tk.END, f"{yeni_musteri.adi} {yeni_musteri.soyadi}")

    def yeni_yemek_ekle(self):
        baslik = simpledialog.askstring("Yeni Yemek Ekle", "Yemek Ismi:")
        icerik = simpledialog.askstring("Yeni Yemek Ekle", "Yemek İçeriği:")
        tarih = simpledialog.askstring("Yeni Yemek Ekle", "Siparis Tarihi:")

        if baslik and icerik and tarih:
            yeni_ders = Yemek(baslik, icerik, tarih)
            self.yemek_listesi.append(yeni_ders)
            self.liste_yemek.insert(tk.END, yeni_ders.baslik)

    def yemek_ata(self):
        selected_musteri_index = self.liste_musteri.curselection()
        #selected_yemek_index = self.liste_yemek.curselection()

        if selected_musteri_index:  # and selected_ders_index
            Musteri = self.musteri_listesi[selected_musteri_index[0]]
            #Yemek = self.yemek_listesi[selected_yemek_index[0]]
            
            Musteri.yemek_ekle(self.yemek_listesi[0])
            print(f"{Musteri.adi} {Musteri.soyadi} adlı Müsteriye {self.yemek_listesi[0].baslik} Siparis edilmistir.")


   

if __name__ == "__main__":
    app = Uygulama()
    
    yeni_musteri_btn = tk.Button(app, text="Yeni Müsteri Ekle", command=app.yeni_musteri_ekle)
    yeni_musteri_btn.pack()

    yeni_yemek_btn = tk.Button(app, text="Yeni Yemek Ekle", command=app.yeni_yemek_ekle)
    yeni_yemek_btn.pack()

    app.mainloop()
