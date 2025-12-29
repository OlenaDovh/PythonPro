discount = 10


def create_order(price: int | float) -> tuple:
    """Calculates the final sum of the order using existing discounts"""
    final_sum = price - (price * discount / 100)
    print(f"Початкова ціна: {price} грн")

    def apply_additional_discount(add_discount):
        """Calculates the final sum of the order using additional discount"""
        nonlocal final_sum
        if add_discount == 0:
            print(f"Додаткових знижок немає. Кінцева ціна з базовою знижкою {discount}%: {final_sum} грн")
            return final_sum
        final_sum = final_sum - (final_sum * add_discount / 100)
        print(f"Кінцева ціна з додатковою знижкою {add_discount}%: {final_sum} грн")
        return final_sum

    return final_sum, apply_additional_discount


order_sum1, additional_discount1 = create_order(1000)
fin_sum1 = additional_discount1(6)

order_sum2, additional_discount2 = create_order(500)
fin_sum2 = additional_discount2(0)
