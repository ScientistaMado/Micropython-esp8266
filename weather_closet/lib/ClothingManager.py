from machine import Pin


class ClothingManager():
    def __init__(self, data_pin, clock_pin, latch_pin):
        self.data_pin = data_pin
        self.clock_pin = clock_pin
        self.latch_pin = latch_pin
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

    def turnOnLed(self):
        self.latch_pin.value(0)

        for status_led in self.clothes:
            self.clock_pin.value(0)
            self.data_pin.value(status_led)
            self.clock_pin.value(1)

        self.latch_pin(1)

    def suggestOutfit(self, weather_info):

        clothes_suggest = {
            1: ["TShirt", "Shorts", "Sandals", "Sneakers"],
            2: ["TShirt", "Pants", "Sneakers", "Vest"],
            3: ["TShirt", "Pants", "Sneakers", "Jacket"],
            4: ["TShirt", "Pants", "Sneakers", "Jacket", "Hoodie"],
            5: ["TShirt", "Pants", "Sneakers", "Jacket", "Parka"],
            6: ["TShirt", "Pants", "Boots", "Jacket", "Parka"],
            7: ["TShirt", "Pants", "Boots", "Hoodie", "Parka"],
            8: ["TShirt", "Pants", "Boots", "Hoodie", "Jacket", "Parka"],
            9: ["TShirt", "Pants", "Boots", "Hoodie", "Jacket", "Parka"],
            10: ["TShirt", "Pants", "AnkleBoots", "Hoodie", "Jacket", "Parka"],
            11: ["TShirt", "Pants", "Boots", "Jacket", "Parka"],
            12: ["TShirt", "Pants", "Boots", "Jacket", "Parka"],
            13: ["TShirt", "Pants", "Boots", "Jacket", "Parka"],
            14: ["TShirt", "Pants", "AnkleBoots", "Hoodie", "Jacket", "Parka"],
            15: ["TShirt", "Pants", "AnkleBoots", "Hoodie", "Jacket", "Parka"],
            16: ["TShirt", "Pants", "AnkleBoots", "Hoodie", "Jacket", "Parka"],
            17: ["TShirt", "Pants", "AnkleBoots", "Hoodie", "Jacket", "Parka"],
            18: ["TShirt", "Pants", "AnkleBoots", "Hoodie", "Jacket", "Parka"],
            19: ["TShirt", "Pants", "AnkleBoots", "Hoodie", "Jacket", "Parka"],
            20: ["TShirt", "Pants", "AnkleBoots", "Hoodie", "Jacket", "Parka"],
            21: ["TShirt", "Pants", "AnkleBoots", "Hoodie", "Jacket", "Parka"],
            22: ["TShirt", "Pants", "AnkleBoots", "Hoodie", "Jacket", "Parka"],
        }
        self.wear(clothes_suggest[weather_info["Símbolo del tiempo"]])
        self.turnOnLed()
