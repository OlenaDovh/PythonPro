subscribers = []


def subscribe(subscr_name: str) -> None:
    """Adds subscriber to the subscription and prints message"""
    subscribers.append(subscr_name)

    def confirm_subscription() -> None:
        print(f"Підписка для {subscr_name} підтверджена")

    confirm_subscription()


def unsubscribe(subscr_name: str) -> None:
    """Removes subscriber from the subscription and prints message"""
    if subscr_name not in subscribers:
        print(f"Підписки для {subscr_name} не знайдено")
    else:
        subscribers.remove(subscr_name)

        def confirm_unsubscription() -> None:
            print(f"{subscr_name} успішно відписаний")

        confirm_unsubscription()


subscribe('Євгенія')
subscribe('Данило')
subscribe('Фіма')
print(subscribers)

unsubscribe('Данило')
print(subscribers)
unsubscribe('Данило')
print(subscribers)
unsubscribe('Анжела')
print(subscribers)
