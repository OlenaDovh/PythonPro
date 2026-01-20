import xml.etree.ElementTree as et


def create_new_xml_file(file_path: str, products: list) -> None:
    """Creates a new XML file with products information."""
    root = et.Element("products")

    for prod in products:
        product = et.SubElement(root, "product")
        name_el = et.SubElement(product, "name")
        price_el = et.SubElement(product, "price")
        quantity_el = et.SubElement(product, "quantity")

        name_el.text = str(prod["name"])
        price_el.text = str(prod["price"])
        quantity_el.text = str(prod["quantity"])

        print(f"Продукт: {name_el.text}, ціна: {price_el.text}, кількість: {quantity_el.text}")

    tree = et.ElementTree(root)
    et.indent(tree)
    tree.write(file_path, encoding="utf-8")


def update_quantity(file_path: str, prod_name: str, new_qnt_val: int) -> None:
    """Updates the quantity of a specific product in the XML file"""

    with open(file_path, 'r', encoding="utf-8") as xml_file:
        tree = et.parse(xml_file)
        root = tree.getroot()

        for product in root.findall("product"):
            name = product.find("name")
            price = product.find("price")
            quantity = product.find("quantity")
            print(f"Продукт: {name.text}, ціна: {price.text}, кількість: {quantity.text}")

            if name is not None and name.text == prod_name:
                quantity.text = str(new_qnt_val)
                print(f"NEW Продукт: {name.text}, ціна: {price.text}, кількість: {quantity.text}")

    with open(file_path, 'wb') as xml_file:
        et.indent(tree)
        tree.write(xml_file, encoding="utf-8", xml_declaration=True)


prods = [
    {"name": "Молоко", "price": 25, "quantity": 50},
    {"name": "Хліб", "price": 10, "quantity": 100}
]

FILE_NAME = "xml_file_1.xml"

create_new_xml_file(FILE_NAME, prods)
print()
update_quantity(FILE_NAME, "Молоко", 20)
