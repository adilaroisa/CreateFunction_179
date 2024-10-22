# 1. 
def konversisuhu(temperature, value): # Mendefinisikan fungsi konversisuhu yang menerima dua parameter, temperature (suhu) dan value
    if value == 'C': # Memeriksa apakah nilai value adalah 'C'. Jika iya, maka akan mengonversi dari Fahrenheit ke Celcius.
        temperaturesuhu = (temperature -32) * 5/9 # untuk mengonversi Fahrenheit ke Celcius. Setelah dihitung, suhu dalam Celcius dan huruf 'C' dikembalikan (return).
        return temperaturesuhu, 'C'
    else:
        temperaturesuhu = (temperature * 9/5) + 32 # Jika nilai value bukan 'C', program akan mengonversi suhu dari Celcius ke Fahrenheit 
        return temperaturesuhu, 'F'
    
celcius_temperature = 30 # Mendefinisikan variabel celcius_temperature sebagai 30°C, lalu memanggil fungsi konversisuhu untuk mengonversi ke Fahrenheit. Hasilnya dicetak dengan format string.
temperaturesuhu, target_value = konversisuhu(celcius_temperature, 'F')
print (f"{celcius_temperature}°C dikonversi ke Fahreinheit adalah {temperaturesuhu}°{target_value} ")

fahreinheit_temperature = 86 # : Mendefinisikan variabel fahreinheit_temperature sebagai 86°F, lalu memanggil fungsi konversisuhu untuk mengonversi ke Celcius. Hasilnya juga dicetak dengan format string.
temperaturesuhu, target_value = konversisuhu(fahreinheit_temperature, 'C')
print (f"{fahreinheit_temperature}°F dikonversi ke celcius adalah {temperaturesuhu}°{target_value}")


# 2. 
import math #library untuk operasi matematika

luas_lingkaran = lambda r: math.pi * r*r # : Mendefinisikan fungsi luas_lingkaran menggunakan lambda (fungsi anonim). Fungsi ini menghitung luas lingkaran berdasarkan jari-jari r dengan rumus.

# Contoh penggunaannya

jari_jari = 7
area = luas_lingkaran(jari_jari)
print(f"Luas lingkaran dengan jari-jari {jari_jari} adalah {area:.2f}")