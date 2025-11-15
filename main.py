class MenyuItem:
    def tayyorlash_vaqti(self):
        raise NotImplementedError

    def narx_hisoblash(self, miqdor):
        raise NotImplementedError

    def allergiya_tekshirish(self, ingredient):
        return False


class Ovqat(MenyuItem):
    def __init__(self, nom, vaqt, narx, allergenlar):
        self.nom = nom
        self.vaqt = vaqt
       	self.narx = narx
        self.allergenlar = allergenlar

    def tayyorlash_vaqti(self):
        return self.vaqt

    def narx_hisoblash(self, miqdor):
        return self.narx * miqdor

    def allergiya_tekshirish(self, ingredient):
        return ingredient.lower() in self.allergenlar


class Ichimlik(MenyuItem):
    def __init__(self, nom, vaqt, narx):
        self.nom = nom
        self.vaqt = vaqt
        self.narx = narx

    def tayyorlash_vaqti(self):
        return self.vaqt

    def narx_hisoblash(self, miqdor):
        return self.narx * miqdor


class Desert(MenyuItem):
    def __init__(self, nom, vaqt, narx):
        self.nom = nom
        self.vaqt = vaqt
        self.narx = narx

    def tayyorlash_vaqti(self):
        return self.vaqt

    def narx_hisoblash(self, miqdor):
        return self.narx * miqdor


menyu = [
    Ovqat("Palov", 25, 30000, ["sabzi", "gosht"]),
    Ichimlik("Choy", 2, 5000),
    Desert("Tort", 10, 20000)
]

buyurtmalar = [
    (0, 2),
    (1, 3),
    (2, 1)
]

umumiy_vaqt = 0
umumiy_narx = 0

for item_index, miqdor in buyurtmalar:
    item = menyu[item_index]
    umumiy_vaqt += item.tayyorlash_vaqti()
    umumiy_narx += item.narx_hisoblash(miqdor)

print(umumiy_vaqt)
print(umumiy_narx)
print(menyu[0].allergiya_tekshirish("sabzi"))
print(menyu[1].allergiya_tekshirish("sabzi"))
