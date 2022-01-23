import validators


class Backpack:
    """Defines backpack and number of available slots; __init__(self, slots=15)"""

    def __init__(self, slots=15):
        self.backpack_slots = []
        self._basic_slots = validators.validate_int_value(slots)
        for slot in range(self._basic_slots):
            slot = "Empty slot"
            self.backpack_slots.append(slot)

    def __repr__(self):
        return f"This is PlayerBackPack class object. ID:{id(self)}"

    @property
    def slots(self):
        return self._basic_slots

    # put item in first empty slot in backpack
    def put_item_into_backpack(self, item):
        for item_slot in range(len(self.backpack_slots)):
            if self.backpack_slots[item_slot] == "Empty slot":
                self.backpack_slots[item_slot] = item
                break
            if item_slot == 14:
                print("No room in inventory")

    # withdraws from backpack item chosen by slot number
    def withdraw_item_from_slot(self, slot_index):
        validators.validate_sack_number_value(slot_index)
        for item_slot in range(len(self.backpack_slots)):
            if (item_slot + 1) == slot_index:
                self.backpack_slots[item_slot] = "Empty slot"

    # extends number of slots in players backpack
    def slot_extender(self, additional_slot):
        for new_slot in range(additional_slot):
            self.backpack_slots.append("Empty slot")

    def show_slots(self):
        for i in self.backpack_slots:
            print(i)


class GoldSack:
    """Creates sack for gold.
    _-init__(self, gold_amount=0) """

    def __init__(self, gold_amount=0):
        self.gold_amount = validators.validate_sack_number_value(gold_amount)

    def __repr__(self):
        return f"Sack with {self.gold_amount} gold"

    # add gold to sack
    def put_gold_into_sack(self, value):
        self.gold_amount = self.gold_amount + validators.validate_sack_number_value(value)

    # withdraw gold from sack
    def withdraw_gold_from_sack(self, value):
        self.gold_amount = self.gold_amount - validators.validate_sack_number_value(value)
        if self.gold_amount < 0:
            self.gold_amount = 0

    # shows amount of gold
    def check_gold_in_sack(self):
        return f"Sack has {self.gold_amount} gold"
