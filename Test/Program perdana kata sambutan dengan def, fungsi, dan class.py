#Buatlah program sambutan mahasiswa dengan class dan def beserta parent dan child class nya.

class murid():
    def __init__(self, name, umur):
        self.name = name
        self.umur = umur

    def sambutan(self):
        print(f"Selamat datang", self.name, ",", "Umur kamu adalah : ", self.umur)
    

x = murid("Aqua", "30")
x.sambutan()

#berikut child class yang mewarisi atau meng inherit atribut daripada parent class dengan tambahan tahun angkatan

class programmurid(murid):
    def __init__(self, name, umur, tahun):
        super().__init__(name, umur)
        self.tahunlulus = tahun
    
    
    def welcome(self):
        print(f"Selamat datang", self.name, ",", "Umur kamu adalah : ", self.umur, "Kamu merupakan angkatan tahun :", self.tahunlulus)
        
menu = programmurid("Farhan", "30", "2020")
menu.welcome()
    