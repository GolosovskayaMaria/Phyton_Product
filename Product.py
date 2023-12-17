import requests

print("\n")

product = input("Введите название продукта: ")

code = {'Nutella': '3017620422003', 'Ketchup': '87157215', 'Twix': '5000159459228'}

if product in code:
    print('Продукт найден', "Код продукта: " + code[product], sep="\n")
    print("\n", "О продукте:", "\n")
    link = requests.get("https://world.openfoodfacts.org/api/v2/product/" + code[product] + '.json')
    result = link.json()
    allergen = result["product"]["allergens"]
    brand = result["product"]["brands"]
    food_group = result["product"]["food_groups"]
    ingredients = result["product"]["ingredients_text_en"]
    print('Ингредиенты: ' + ingredients, 'Группа продуктов: ' + food_group, 'Бренд: ' + brand, 'Аллергены: ' + allergen, sep="\n")
elif product == "":
    print('Ошибка. Введите название продукта', "\n")
else:
    print('Ошибка. Продукт не найден', "\n")
