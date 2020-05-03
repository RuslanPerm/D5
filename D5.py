class Shop:
    def __init__(self):
        self.products = None
        self.coasts = None
        self.quantity = None
        self.name, self.shop, self.product, self.count, self.save_check = None, None, None, None, None

    def counting(self):
        for i in range(len(self.quantity)):
            if self.quantity[i] == 0:
                del self.products[i]
                del self.coasts[i]

    def user_buy(self, user_name, shop_name, product_name, count, save_check=False):
        self.name = user_name
        self.shop = shop_name
        self.product = product_name
        self.count = count
        self.save_check = save_check

    def save_changes(self, file_name):
        pass

    def load_data(self, file_name, rewrite=False):
        pass

    def find_product(self, product_name, count=-1):
        useful_shops = []
        for i in shops:
            for j in range(len(i.products)):
                if (i.products[j] == product_name) and (i.quantity[j] > 0):
                    useful_shops.append(i)
        return useful_shops

# по логике, в ходе работы программы, ошибок возникнуть не должно т.к. значениями i будут классы

    def find_products(self, products):
        useful_shops = []
        pass

    def sort_shops_by_product_price(self, product):
        minimum, sorted_lst = 10 ** 19, []
        shops_with_product = self.find_product(product) # ищет магазины, в которых есть этот продуктsss
        for i in shops_with_product:
            sorted_lst.append(i.coasts[i.products.index(product)])
            # берётся индекс искомого продукта из класса магазина из списка продуктов, и с таким же
            # индексом цена этого продукта из списка цен
        return sorted(sorted_lst)

    def sort_shops_by_product_count(self, product):
        pass


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


class Bigboishop(Shop):
    def __init__(self, products, coasts, quantity):
        super().__init__(products, coasts, quantity)
        self.products = ["Война и Мир", "Зверобой", "Do what u r", "STFU", "Самоделкин", "Мандалорец", "Волкодав"]
        self.coasts = [5000, 3100, 1999, 300, 100, 9999, 2700]
        self.quantity = [4, 9, 2, 10, 2, 4, 8]


shops = [Uyut, Prada, Nezachetochka, Bigboishop]

a = Shop()
a.find_product("маска")
