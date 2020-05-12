from datetime import datetime


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
        if count > 0:
            if shop_name.quantity[shop_name.products.index(product_name)] >= count:
                print(shop_name.quantity[shop_name.products.index(product_name)])
                shop_name.quantity[shop_name.products.index(product_name)] -= count
                print(shop_name.quantity[shop_name.products.index(product_name)])
                if save_check is True:
                    date_and_time = str(datetime.today()).split()

                    date = date_and_time[0]
                    time = date_and_time[1][:8]
                    time = [x for x in time]
                    for _ in time:
                        if _ == ':':
                            time[time.index(_)] = '-'
                    time = ''.join(time)

                    with open(f"{user_name}_{date}_{time}.txt", "w", encoding='utf-8') as file:
                        file.write(f'купленный товар: {product_name}\nкол-во товара: {count}\nмагазин: {shop_name}')
                    file.close()
            else:
                print("В магазине меньшее кол-во товара, что Вы просите")
        else:
            print("Не вижу смысла в Вашей покупке")

    def save_changes(self, file_name):
        with open(f"{file_name}.txt", "w", encoding='utf-8') as file:
            for elem in shops:
                file.write(f'В магазине {elem}:\n')
                for _ in range(len(elem.products)-1):
                    file.write(f'{elem.products[_]} - {elem.quantity[_]} штук\n')
                file.write('\n')

        file.close()

    def load_data(self, file_name, rewrite=False):
        pass

    def find_product(self, product_name, should_i_print=True, count=0):
        useful_shops = []
        for i in shops:
            for j in range(len(i.products)):
                if (i.products[j] == product_name) and (i.quantity[j] > count):
                    useful_shops.append(i)
        if should_i_print is True:
            print(*useful_shops, sep='\n')
        return useful_shops

    def find_products(self, products):
        useful_shops = set()
        black_list = []
        for product in products:
            shops_with_elem = self.find_product(product)
        pass

    def sort_shops_by_product_price(self, product):
        price_lst = []
        shops_with_product = self.find_product(product, False) # ищет магазины, в которых есть этот продукт
        for i in shops_with_product:
            price_lst.append(i.prices[i.products.index(product)])
            # берётся индекс искомого продукта из класса магазина из списка продуктов, и с таким же
            # индексом цена этого продукта из списка цен
        for j in range(len(shops_with_product)):
            print(f'{shops_with_product[price_lst.index(min(price_lst))]}: {min(price_lst)} рублей')
            if len(price_lst) > 1:
                index_for_delete = price_lst.index(min(price_lst))
                price_lst.pop(index_for_delete)
                shops_with_product.pop(index_for_delete)

    def sort_shops_by_product_count(self, product):
        quantity_lst = []
        shops_with_product = self.find_product(product, False)  # ищет магазины, в которых есть этот продукт
        for i in shops_with_product:
            quantity_lst.append(i.quantity[i.products.index(product)])
            # берётся индекс искомого продукта из класса магазина из списка продуктов, и с таким же
            # индексом цена этого продукта из списка цен
        for j in range(len(shops_with_product)):
            print(f'{shops_with_product[quantity_lst.index(max(quantity_lst))]}: {max(quantity_lst)} штук')
            if len(quantity_lst) > 1:
                index_for_delete = quantity_lst.index(max(quantity_lst))
                quantity_lst.pop(index_for_delete)
                shops_with_product.pop(index_for_delete)


class Moydodyr(Shop):
    def __init__(self):
        super().__init__()
        self.products = ['моющее средство', 'мыло', 'маска', 'зубная паста', 'вода', 'шампунь', 'гель для душа']
        self.prices = [300, 100, 5000, 58, 7, 120, 300]
        self.quantity = [18, 50, 102, 33, 78, 4, 80]


class Prada(Shop):
    def __init__(self):
        super().__init__()
        self.products = ["сумка", "куртка", "маска", "шапка", "ремень", "кошель", "футболка", "STFU"]
        self.prices = [10000, 23000, 9999, 10, 3467, 9123, 4823, 79999]
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
        self.products = ["Война и Мир", "Зверобой", "Do what u r", "STFU", "Мандалорец", "Волкодав", "газеты", "маска"]
        self.prices = [5000, 3100, 1999, 300, 100, 9999, 2700, 900]
        self.quantity = [4, 9, 2, 10, 2, 4, 8, 42]


shops = [Moydodyr(), Prada(), Nezachetochka(), Bigboishop()]

a = Shop()
# a.find_product("маска")
# a.sort_shops_by_product_price("маска")
# a.sort_shops_by_product_count('маска')
a.user_buy('ruslan', Nezachetochka(), 'маска', 6)
# print(Nezachetochka().quantity[Nezachetochka().products.index('маска')])
# a.save_changes('data')
