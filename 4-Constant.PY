from typing import Final

VERSION: Final[str] = "1.0.12"
PHI: Final[float] = 3.1415

def hitung_luas_lingkaran(jari_jari: float) -> float:
    return PHI * jari_jari ** 2

def hitung_keliling_lingkaran(jari_jari: float) -> float:
    return 2 * PHI * jari_jari

def hitung_luas_persegi(sisi: float) -> float:
    return sisi ** 2

print(hitung_luas_lingkaran(5)) # 78.5375
print(hitung_keliling_lingkaran(5)) # 31.415
print(hitung_luas_persegi(5)) # 25.0

