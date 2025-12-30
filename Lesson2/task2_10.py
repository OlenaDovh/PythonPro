from typing import Callable


def create_product(name: str) -> Callable:
    """Creates new product with its name, price and count"""

    def set_product_price(price: int | float) -> Callable:
        def set_count(count: int) -> tuple:
            new_product = {
                'name': name,
                'price': price,
                'count': count
            }

            def set_new_price(price_new: int | float) -> None:
                """Changes price of the product"""
                new_product['price'] = price_new
                print(f"New price of '{name}' is {new_product['price']}")

            def get_product() -> dict:
                """Gives info of the product (name, price, count)"""
                return new_product

            return set_new_price, get_product

        return set_count

    return set_product_price


create_book1 = create_product('The Widow by John Grisham')
book_price1 = create_book1(360)
set_price1, get_product1 = book_price1(15)
print(get_product1())
set_price1(520)
print(get_product1())

print('--------------------')

create_book2 = create_product('The Housemaid by Freida McFadden')
book_price2 = create_book2(870)
set_price2, get_product2 = book_price2(7)
print(get_product2())
set_price2(600)
print(get_product2())
