class ClothingManager():
    def __init__(self):
        self.clothes = [0] * 14
        self.clothing_mapping = {
            "RainBoots": 0,
            "Boots": 1,
            "AnkleBoots": 2,
            "Parka": 3,
            "Coat": 4,
            "Jacket": 5,
            "Sandals": 6,
            "Sneakers": 7,
            "Shorts": 8,
            "Pants": 9,
            "Vest": 10,
            "Hoodie": 11,
            "LSTShirt": 12,
            "TShirt": 13
        }

    def wear(self, *clothes):
        self.clothes = [0] * 14  # Reiniciar la lista de ropa
        for clothe in clothes:
            if clothe in self.clothing_mapping:
                position = self.clothing_mapping[clothe]
                self.clothes[position] = 1
            else:
                print(f"Prenda no válida: {clothe}")
        return self.clothes
