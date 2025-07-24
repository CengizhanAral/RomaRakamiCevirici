import tkinter as tk
from tkinter import messagebox
import re

class RomanToIntegerConverter:
    def __init__(self, master):
        self.master = master
        master.title("Roma Rakamı Çevirici")
        master.geometry("400x200")
        master.resizable(False, False)

        # Roma rakamı değerleri sözlüğü
        self.roman_map = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
        }

        self.label_input = tk.Label(master, text="Roma Rakamını Girin:")
        self.label_input.pack(pady=4)

        self.entry_roman = tk.Entry(master, width=40)
        self.entry_roman.pack(pady=2)

        self.button_convert = tk.Button(master, text="Dönüştür", command=self.convert_roman)
        self.button_convert.pack(pady=1)

        self.label_result = tk.Label(master, text="Sonuç:")
        self.label_result.pack(pady=15)

        self.label_rules = tk.Label(master, text="Roma rakamları hakkında yardım mı lazım?")
        self.label_rules.pack(pady=1)

        self.button_rules = tk.Button(master, text="Kurallar", command=self.display_rules)
        self.button_rules.pack(pady=1)

    def convert_roman(self):
        roman_num = self.entry_roman.get().upper()

        # Boş giriş kontrolü
        if not roman_num:
            messagebox.showerror("Hata", "Bir Roma rakamı girin.")
            self.label_result.config(text="Sonuç: 0")
            return

        # Geçersiz karakter kontrolü
        for char in roman_num:
            if char not in self.roman_map:
                messagebox.showerror("Hata", "Geçersiz karakter. Sadece I, V, X, L, C, D, M kullanın.")
                self.label_result.config(text="Sonuç: Olmayan sayı")
                return

        # Roma rakamı format kuralları kontrolü
        if not self._is_valid_roman(roman_num):
            messagebox.showerror("Hata", "Geçersiz Roma rakamı formatı. Lütfen Roma rakamı kurallarına uygun girin.")
            self.label_result.config(text="Sonuç: Hatalı sayı")
            return

        # Dönüşüm işlemini yap
        result = self._roman_to_int(roman_num)

        # Sonuçta herhangi bir aksaklık var mı kontrolü
        if result is None:
            messagebox.showerror("Bilinmeyen Hata", "Dönüşüm sırasında beklenmeyen bir hata oluştu.")
            self.label_result.config(text=f"Sonuç: {result} \n UwU")
        else:
            self.label_result.config(text=f"Sonuç: {result}")

    def _roman_to_int(self, s: str) -> int:
        total = 0
        prev_value = 0
        for char in reversed(s):
            current_value = self.roman_map[char]
            # Bu kısımda çıkartmalı roma sayıları işlenir.
            if current_value < prev_value:
                total -= current_value
            # Bu kısımda toplamalı roma sayıları işlenir.
            else:
                total += current_value
            prev_value = current_value
        return total

    def _is_valid_roman(self, s: str) -> bool:
        # Bu fonksiyon, Roma rakamlarının yazım kurallarını kontrol etmektedir.
        pattern = re.compile(r"^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$")
        return bool(pattern.match(s))

    def display_rules(self):
        rules_window = tk.Toplevel(self.master)
        rules_window.title("Roma Rakamı Kuralları")
        rules_window.geometry("550x800")
        rules_window.resizable(False, False)
        rules_widget = tk.Text(rules_window, wrap="word", padx=10, pady=10)
        rules_widget.pack(expand=True, fill="both")
        rules_content = """Roma Rakamı Kuralları:

    1.  Temel Rakamlar:
        I = 1, V = 5, X = 10, L = 50, C = 100, D = 500, M = 1000

    2.  Tekrar Etme Kuralı:
        * I, X, C, M rakamları en fazla üç kez art arda yazılabilir.
            Örnek: III = 3, XXX = 30, CC = 200
        * V, L, D rakamları art arda yazılamaz.

    3.  Toplama Kuralı:
        * Büyük değerli bir rakamın sağına daha küçük değerli bir rakam yazılırsa, değerler toplanır.
            Örnek: VI = 5 + 1 = 6, LXI = 50 + 10 + 1 = 61

    4.  Çıkarma Kuralı:
        * Sadece I, X, C rakamları kendilerinden daha büyük olan bir rakamın soluna yazılabilir ve bu durumda büyük rakamdan küçük rakamın değeri çıkarılır.
        * I sadece V veya X'ten çıkarılabilir.
            Örnek: IV = 5 - 1 = 4, IX = 10 - 1 = 9
        * X sadece L veya C'den çıkarılabilir.
            Örnek: XL = 50 - 10 = 40, XC = 100 - 10 = 90
        * C sadece D veya M'den çıkarılabilir.
            Örnek: CD = 500 - 100 = 400, CM = 1000 - 100 = 900
        * V, L, D rakamları asla çıkarılamaz.
        * Bir rakamın soluna sadece bir rakam yazılabilir.
            Örnek: IX, CD, XLIX, MMMCMXCIX

    5.  Sıralama Kuralı:
        * Rakamlar çıkarma kuralı dışında büyükten küçüğe doğru yazılır.
        * Örnek: MCMXCIX = 1999, MMXXV = 2025


Ondalık Basamak Yapısı:

    Binler | Yüzler | Onlar | Birler
    M      | C      | X     | I
    MM     | CC     | XX    | II
    MMM    | CCC    | XXX   | III
           | CD     | XL    | IV
           | D      | L     | V
           | DC     | LX    | VI
           | DCC    | LXX   | VII
           | DCCC   | LXXX  | VIII
           | CM     | XC    | IX"""

        rules_widget.insert("end", rules_content)


def main():
    root = tk.Tk()
    app = RomanToIntegerConverter(root)
    root.mainloop()

if __name__ == "__main__":
    main()
