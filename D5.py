class Shop:
    def __init__(self, products, coasts, quantity):
        self.products = products
        self.coasts = coasts
        self.quantity = quantity

    def counting(self):
        for i in range(len(self.quantity)):
            if self.quantity[i] == 0:
                del self.products[i]
                del self.coasts[i]


class Uyut(Shop):
    def __init__(self, products, coasts, quantity):
        super().__init__(products, coasts, quantity)
        self.products = ['моющее средство', 'мыло', 'маска', 'зубная паста', 'вода', 'шампунь', 'гель для душа']
        self.coasts = [300, 100, 5000, 58, 7, 120, 300]
        self.quantity = [18, 50, 102, 33, 78, 4, 80]


class Prada(Shop):
    def __init__(self, products, coasts, quantity):
        super().__init__(products, coasts, quantity)
        self.products = ["сумка", "куртка", "маска", "шапка", "ремень", "кошель", "футболка", "платье"]
        self.coasts = [10000, 23000, 999990, 10, 3467, 9123, 4823, 79999]
        self.quantity = [10, 2, 1, 3700, 12, 8, 1000]


class Nezachetochka(Shop):
    def __init__(self, products, coasts, quantity):
        super().__init__(products, coasts, quantity)
        self.products = ["круассан", "хлеб", "масло", "молоко", "вода", "чай", "йогурт", "маска", "мыло", "футболка"]
        self.coasts = [34, 20, 400, 50, 20, 100, 49, 99, 1999, 1]
        self.quantity = [8, 12, 50, 17, 100, 288, 43, 35, 9, 102323]