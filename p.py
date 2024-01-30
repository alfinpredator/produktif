class Hewan:
    def __init__(self, nama, jenis):
        self.nama = nama
        self.jenis = jenis

    def bersuara(self):
        pass

class Mamalia(Hewan):
    def __init__(self, nama, jenis, mamalia_type):
        super().__init__(nama, jenis)
        self.mamalia_type = mamalia_type

    def menyusui(self):
        print(f"{self.nama} adalah mamalia yang menyusui.")

    def bersuara(self):
        print(f"{self.nama} bersuara: Bunyi mamalia")

class Burung(Hewan):
    def __init__(self, nama, jenis, burung_type):
        super().__init__(nama, jenis)
        self.burung_type = burung_type

    def terbang(self):
        print(f"{self.nama} dapat terbang.")

    def bersuara(self):
        print(f"{self.nama} bersuara: Kicau kicau")

# Penggunaan kelas
kucing = Mamalia("Kucing", "Karnivora", "Mamalia")
elang = Burung("Elang", "Karnivora", "Burung")

kucing.menyusui()
kucing.bersuara()

elang.terbang()
elang.bersuara()
