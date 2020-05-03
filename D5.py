class Shop:
    def __init__(self, products=None, prices=None, quantity=None):
        self.products = products
        self.prices = prices
        self.prices = prices
        self.quantity = quantity
        self.name, self.shop, self.product, self.count, self.save_check = None, None, None, None, None

    def __str__(self):
        return f"{self.__class__.__name__}"
        # return f"{self.__class__.__name__}\nproducts: {', '.join(map(str, self.products))}
        # \nprices: {', '.join(map(str, self.prices))} \nquantity: {','.join(map(str, self.quantity))}\n"

    def counting(self):
        for i in range(len(self.quantity)):
            if self.quantity[i] == 0:
                del self.products[i]
                del self.prices[i]

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
        # for k in useful_shops:
        #     print(k)
        print(*useful_shops, sep='\n')
        return useful_shops

    def find_products(self, products):
        useful_shops = []
        pass

    def sort_shops_by_product_price(self, product):
        minimum, sorted_lst = 10 ** 19, []
        shops_with_product = self.find_product(product) # ищет магазины, в которых есть этот продуктsss
        for i in shops_with_product:
            sorted_lst.append(i.prices[i.products.index(product)])
            # берётся индекс искомого продукта из класса магазина из списка продуктов, и с таким же
            # индексом цена этого продукта из списка цен
        print(sorted(sorted_lst))

    def sort_shops_by_product_count(self, product):
        pass


class CleaningSnake(Shop):
    def __init__(self):
        super().__init__()
        self.products = ['моющее средство', 'мыло', 'маска', 'зубная паста', 'вода', 'шампунь', 'гель для душа']
        self.prices = [300, 100, 5000, 58, 7, 120, 300]
        self.quantity = [18, 50, 102, 33, 78, 4, 80]


class Prada(Shop):
    def __init__(self):
        super().__init__()
        self.products = ["сумка", "куртка", "маска", "шапка", "ремень", "кошель", "футболка", "платье"]
        self.prices = [10000, 23000, 999990, 10, 3467, 9123, 4823, 79999]
        self.quantity = [10, 2, 1, 3700, 12, 8, 1000]


class Nezachetochka(Shop):
    def __init__(self):
        super().__init__()
        self.products = ["круассан", "хлеб", "масло", "молоко", "вода", "газеты", "йогурт", "маска", "мыло", "футболка"]
        self.prices = [34, 20, 400, 50, 20, 100, 49, 99, 1999, 1]
        self.quantity = [8, 12, 50, 17, 100, 288, 43, 35, 9, 102323]


class Bigboishop(Shop):
    def __init__(self):
        super().__init__()
        self.products = ["Война и Мир", "Зверобой", "Do what u r", "STFU", "Мандалорец", "Волкодав", "газеты"]
        self.prices = [5000, 3100, 1999, 300, 100, 9999, 2700]
        self.quantity = [4, 9, 2, 10, 2, 4, 8]


shops = [CleaningSnake(), Prada(), Nezachetochka(), Bigboishop()]

a = Shop()
a.find_product("маска")
