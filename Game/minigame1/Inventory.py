import json

class Inventory:

    def __init__(self, slot_1, slot_2, slot_3):
        self.slot_1 = slot_1
        self.slot_2 = slot_2
        self.slot_3 = slot_3

    def updateInventory (self, slot_1, slot_2, slot_3):
        self.slot_1 = slot_1
        self.slot_2 = slot_2
        self.slot_3 = slot_3

    def clearInventory(self):
        self.slot_1 = {"name" : "", "img" : ""}
        self.slot_2 = {"name" : "", "img" : ""}
        self.slot_3 = {"name" : "", "img" : ""}

