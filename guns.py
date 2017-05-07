from firearm import Firearm


class Pistol(Firearm):
    base_sale_price = 1000

    def firearm_type(self):
        return 'pistol'


pistol = Pistol(11, 20, 10, 2004)
print(pistol.sale_price())
