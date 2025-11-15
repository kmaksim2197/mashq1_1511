# Restoran Menyusi – Polimorfizm Misoli (Python)

## Tavsif
Ushbu loyiha restoran menyusi elementlarini OOP yordamida modellashtiradi. Loyiha quyidagi sinflardan tashkil topgan:

- Ovqat
- Ichimlik
- Desert

Har bir sinf umumiy `MenyuItem` bazaviy sinfidan meros oladi va quyidagi metodlarga ega:

- `tayyorlash_vaqti()` – elementni tayyorlash vaqtini qaytaradi
- `narx_hisoblash(miqdor)` – buyurtma narxini hisoblaydi
- `allergiya_tekshirish(ingredient)` – faqat Ovqat sinfida ishlaydi, boshqalari False qaytaradi

Polimorfizm orqali barcha menyu elementlari bitta ro‘yxat orqali boshqariladi.

---

## Funksionallik

- Menyu elementlari yaratiladi va ro‘yxatga joylanadi.
- Buyurtmalar `(index, miqdor)` ko‘rinishida beriladi.
- Tsikl yordamida umumiy:
  - tayyorlash vaqti
  - narx  
  hisoblanadi.
- Ovqat sinfi allergen tekshira oladi.

---

## Ishga tushirish

```bash
python main.py
