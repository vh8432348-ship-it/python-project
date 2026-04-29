# Завдання 1


class Recipe:
    def __init__(self, name, ingredients, text, time):
        self.__name = name
        self.__ingredients = ingredients
        self.__text = text
        self.__time = time

    def get_time(self):
        return self.__time

    def get_name(self):
        return self.__name

    def __str__(self):
        return self.__name

    def __contains__(self, item):
        return item in self.__ingredients

    def __gt__(self, other):
        return self.__time > other.__time

    def display_info(self):
        print(f"Назва: {self.__name}")
        print(f"Інгредієнти: {', '.join(self.__ingredients)}")
        print(f"Рецепт: {self.__text}")
        print(f"Час приготування: {self.__time} хв")
        print("-" * 40)


recipe1 = Recipe(
    "Піца",
    ["борошно", "вода", "дріжджі", "томат", "сир"],
    "Готуємо тісто, додаємо інгредієнти та запікаємо",
    30,
)

recipe2 = Recipe(
    "Салат",
    ["томат", "огірок", "зелень", "олія"],
    "Нарізаємо овочі, додаємо зелень та поливаємо олією",
    10,
)

recipe3 = Recipe(
    "Суп",
    ["вода", "картопля", "морква", "м'ясо"],
    "Варимо всі інгредієнти до готовності",
    45,
)

recipes = [recipe1, recipe2, recipe3]


print("Рецепти, які містять томат:")
for recipe in recipes:
    if "томат" in recipe:
        print(recipe)

print("\nРецепт з найменшим часом приготування:")
fastest_recipe = min(recipes, key=lambda r: r.get_time())
fastest_recipe.display_info()
