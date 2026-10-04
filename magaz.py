from abc import ABC, abstractmethod


class ProductBase(ABC):
    @abstractmethod
    def info(self):
        pass


class Product(ProductBase):
    def __init__(self, name, price, quantity, category):
        self.__name = name
        self.set_price(price)
        self.set_quantity(quantity)
        self.__category = category

    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price

    def get_quantity(self):
        return self.__quantity

    def get_category(self):
        return self.__category

    def set_name(self, name):
        self.__name = name

    def set_category(self, category):
        self.__category = category

    def set_price(self, price):
        if price <= 0:
            raise ValueError('Цена должна быть больше нуля')
        self.__price = price

    def set_quantity(self, quantity):
        if quantity < 0:
            raise ValueError('Кол-во товара не может быть отрицательным')
        self.__quantity = quantity

    def info(self):
        return (f'Название: {self.__name}\n'
                f'Цена: {self.__price} сом\n'
                f'Количество: {self.__quantity} шт.\n'
                f'Категория: {self.__category}')


class FoodProduct(Product):
    def __init__(self, name, price, quantity, expiration_date):
        super().__init__(name, price, quantity, 'Еда')
        self.expiration_date = expiration_date

    def info(self):
        return super().info() + f'\nСрок годности: {self.expiration_date}'


class ElectronicProduct(Product):
    def __init__(self, name, price, quantity, warranty):
        super().__init__(name, price, quantity, 'Электроника')
        self.warranty = warranty

    def info(self):
        return super().info() + f'\nГарантия: {self.warranty}'


class Store():
    def __init__(self):
        self.products = []

    def create_product(self, product):
        self.products.append(product)

    def show_products(self):
        if not self.products:
            print("В магазине пока нет товаров")
            return
        for product in self.products:
            print(product.info())
            print()

    def find_product(self, name):
        for product in self.products:
            if product.get_name().lower() == name.lower():
                return product
        return None

    def update_product(self, name):
        product = self.find_product(name)
        if product is None:
            print("Товар не найден")
            return

        try:
            new_price = input("Новая цена (Enter, чтобы не менять): ")
            if new_price:
                product.set_price(float(new_price))

            new_quantity = input("Новое количество (Enter, чтобы не менять): ")
            if new_quantity:
                product.set_quantity(int(new_quantity))
        except ValueError as e:
            print("Ошибка:", e)

    def delete_product(self, name):
        product = self.find_product(name)
        if product is None:
            print("Товар не найден")
            return
        self.products.remove(product)
        print(f"Товар {name} удалён")

    def search(self):
        poisk = input('Введите название продукта: ')
        product = self.find_product(poisk)
        if product is None:
            print('Такого товара нет')
            return
        print(product.info())

    def sort_price(self):
        if not self.products:
            print('В магазине пока нет товаров')
            return

        sorted_products = sorted(self.products, key=lambda product: product.get_price())
        for product in sorted_products:
            print(product.info())
            print()

    def sort_name(self):
        if not self.products:
            print('В магазине пока нет товаров')
            return
        sorted_name = sorted(self.products, key=lambda product: product.get_name().lower())
        for product in sorted_name:
            print(product.info())
            print()

    def expensive_products(self):
        if not self.products:
            print('В магазине пока нет товаров')
            return

        try:
            vvod = float(input('Введите минимальную цену: '))
        except ValueError:
            print('Ошибка: нужно ввести число')
            return

        sorted_expensive = [product for product in self.products if product.get_price() > vvod]

        if not sorted_expensive:
            print('Товаров дороже этой цены нет')
            return

        for product in sorted_expensive:
            print(product.info())
            print()

    def total_cost(self):
        total = 0
        for product in self.products:
            total += product.get_price() * product.get_quantity()
        return total

    def total_quantity(self):
        total = 0
        for product in self.products:
            total += product.get_quantity()
        return total


menu = """
1. Добавить товар
2. Показать товары
3. Изменить товар
4. Удалить товар
5. Поиск товара
6. Сортировка по цене
7. Сортировка по названию
8. Показать товары дороже заданной суммы
9. Показать общую стоимость склада
10. Показать общее количество товаров
0. Выход
"""


def add_product_menu(store):
    print('Тип товара: 1 - обычный, 2 - еда, 3 - электроника')
    kind = input('Выберите тип: ')

    if kind not in ('1', '2', '3'):
        print('Неверный тип товара')
        return

    name = input('Название: ')
    try:
        price = float(input('Цена: '))
        quantity = int(input('Количество: '))

        if kind == '1':
            category = input('Категория: ')
            product = Product(name, price, quantity, category)
        elif kind == '2':
            expiration_date = input('Срок годности: ')
            product = FoodProduct(name, price, quantity, expiration_date)
        else:
            warranty = input('Гарантия: ')
            product = ElectronicProduct(name, price, quantity, warranty)

        store.create_product(product)
        print('Товар добавлен')
    except ValueError as e:
        print('Ошибка:', e)


def main():
    store = Store()

    while True:
        print(menu)
        choice = input('Выберите действие: ')

        if choice == '0':
            print('bye broke!')
            break
        elif choice == '1':
            add_product_menu(store)
        elif choice == '2':
            store.show_products()
        elif choice == '3':
            name = input('Название товара: ')
            store.update_product(name)
        elif choice == '4':
            name = input('Название товара: ')
            store.delete_product(name)
        elif choice == '5':
            store.search()
        elif choice == '6':
            store.sort_price()
        elif choice == '7':
            store.sort_name()
        elif choice == '8':
            store.expensive_products()
        elif choice == '9':
            print(f'Общая стоимость склада: {store.total_cost()} сом')
        elif choice == '10':
            print(f'Общее количество товаров: {store.total_quantity()} шт.')
        else:
            print('Неверный пункт меню')


if __name__ == '__main__':
    main()