""" import matplotlib.pyplot as plt
import numpy as np

bulan = np.array(["January", "Februari", "Maret", "April", "Mei", "Juni"])
penjualan_a = np.array([120, 130, 150, 110, 135, 120])
penujualan_b = np.array([100, 115, 130, 105, 125, 115])

plt.xticks(np.arange(len(bulan)), bulan) # Berfungsi untuk menghitung jumlah array yang ada di variabel bulan, sehingga bisa disesuaikan dengan kolom x
plt.plot(penjualan_a, "o-r")
plt.plot(penujualan_b, "o-b")
plt.title("Grafik Penjualan Bulanan")
plt.xlabel("Bulan")
plt.ylabel("Penjualan")
plt.grid(axis = "y")
plt.show()

"""

""" import matplotlib.pyplot as plt
import numpy as np

jam_belajar = ([2, 3, 1, 4, 5, 3, 6, 2, 4, 5])
skor_ujian = ([70, 85, 60, 90, 95, 80, 98, 75, 88, 92])
colors = ([0, 10, 20, 30, 40, 50, 60 ,70, 80, 90])

plt.scatter(jam_belajar, skor_ujian, c = colors, cmap = "viridis")
plt.title("Grafik nilai rata rata menurut jam belajar siswa terhadap materi matematika".title())
plt.show() 

"""

import matplotlib.pyplot as plt
import numpy as np

suhu_rata_rata_kota_a = np.random.normal(27,1,365)
suhu_rata_rata_kota_b = np.random.normal(26,1,365)

plt.subplot(3, 2, 1,)
plt.plot(suhu_rata_rata_kota_a)
plt.title("Suhu rata rata kota A".title())

plt.subplot(3, 2, 2)
plt.plot(suhu_rata_rata_kota_b)
plt.title("Suhu rata rata kota B".title())

suhu_maksimum_kota_a = np.random.normal(32,1,365)
suhu_maksimum_kota_b = np.random.normal(31,1,365)

plt.subplot(3, 2, 3)
plt.plot(suhu_maksimum_kota_a)
plt.title("Suhu maksimum kota A".title())

plt.subplot(3, 2, 4)
plt.plot(suhu_maksimum_kota_b)
plt.title("Suhu maksimum kota B".title())


suhu_minimum_kota_a = np.random.normal(22,1,365)
suhu_minimum_kota_b = np.random.normal(20,1,365)

plt.subplot(3, 2, 5)
plt.plot(suhu_minimum_kota_a)
plt.title("Suhu minimum kota A".title())

plt.subplot(3, 2, 6)
plt.plot(suhu_minimum_kota_b)
plt.title("Suhu minimum kota B".title())

plt.suptitle("Grafik suhu ditiap kota selama 1 tahun".title())
plt.show()
