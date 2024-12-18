class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return (f'Название - {self.name}'
                f'\nВес - {self.weight}'
                f'\nКатегория - {self.category}')


class Shop:
    def __init__(self, file_name='products.txt'):
        self.__file_name = file_name

    def get_products(self):
        with open(self.__file_name, 'r', encoding='utf-8') as my_file:
            read_file = my_file.read()
        return read_file

    def add(self, *products):
        product_list = self.get_products().split()
        for product in products:
            if product.name in product_list:
                print(f'Продукт {product.name} уже есть в магазине')
            else:
                file = open(self.__file_name, 'a')
                file.write('\n' + str(product))
                file.close()


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)  # __str__

s1.add(p1, p2, p3)

print(s1.get_products())
