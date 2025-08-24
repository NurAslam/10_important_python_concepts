name: str = "Aslam"
# Karena type annotation di Python hanya petunjuk (hint), bukan aturan wajib. 
# Python tetap dynamically typed, jadi tipe data bisa saja tidak sesuai dengan annotation.
age: int = "eleven"
# tetap bisa jalan
print(age)


# contoh yang benar
name: str = "Aslam"
age: int = 25
tinggi: float = 175.5
is_active: bool = True

def sapa(nama:str, umur:int) -> str: # mengembalikan string
    return f"Halo, nama saya {nama} dan saya {umur} tahun"

def hitung_luas_persegi(sisi:float) -> float: # mengembalikan float
    return sisi * sisi

# Menggunakan Optinoal dan Union
from typing import Optional, Union

def cetak_nilai(nilai: Optional[int]) -> None: # artinya nilai bisa int atau None
    if nilai is None:
        print("Nilai tidak tersedia")
    else:
        print(f"Nilai: {nilai}")

def process_data(data: Union[str, int])-> None: # artinya data bisa str atau int
    print(f"Data: {data}")

print(process_data("100")) # Data: 100
print(process_data(100)) # Data: 100