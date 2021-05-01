
class VendingMachine:

    def __init__(self):
        self.storage = {'Coke': 0, 'Orange Juice': 0, 'Kitkat Chunky Bar': 0, "Lays Classic Chips": 0}
        self.msg = 'Empty VM Started'
        self.errorExist = False
        self.currentItem = ''

    def checkStatus(self):
        if self.errorExist:
            self.msg = f"Invalid product: {self.currentItem}"
        return self.msg

    def checkStock(self, item=None):
        if item is not None:
            if item in self.storage:
                msg = f'{item} ({self.storage[item]})'
            else:
                msg = f"Invalid product: {item}"
        else:
            msg = f"Stock: Coke ({self.storage['Coke']}), Orange Juice ({self.storage['Orange Juice']}), " \
                  f"Kitkat Chunky Bar ({self.storage['Kitkat Chunky Bar']}), " \
                  f"Lays Classic Chips ({self.storage['Lays Classic Chips']})"

        return msg

    def add(self, item, quantity):
        self.errorExist = False
        self.currentItem = item
        if item in self.storage:
            self.storage[item] += quantity
            self.msg = f"Product added: {item} ({quantity})"
        else:
            self.errorExist = True

    def dispense(self, item, quantity):
            self.errorExist = False
            self.currentItem = item
            if item in self.storage:
                self.storage[item] -= quantity
                self.msg = f"Product removed: {item} ({quantity})"
            else:
                self.errorExist = True