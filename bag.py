class Bag:
    def __init__(self):
        self.items = []

    def addItem(self, item):
        new_bag = Bag()
        new_bag.items = self.items.copy()
        new_bag.items.append(item)
        return new_bag

    def totalBenefit(self):
        total = 0
        for item in self.items:
            if item.included:
                total = total + item.benefit
        return total

    def totalWeight(self):
        total = 0
        for item in self.items:
            if item.included:
                total = total + item.weight
        return total

    def getIncludedItems(self):
        items_inc = []
        for item in self.items:
            if item.included:
                items_inc.append(item)
        return items_inc
