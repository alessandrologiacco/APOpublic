from typing import Callable
from diet.nutritional import NutritionalElement


class Recipe(NutritionalElement):

    def __init__(self, name: str, food: "Food") -> None:
        self._name = name
        self._food = food
        self._ingredients = {}

    def add_ingredient(self, raw_material_name: str, quantity: float) -> "Recipe":
        self._ingredients[raw_material_name] = quantity
        return self

    def calculate_nutritional_value(self, get_nutritional_value: Callable):
        total_value = 0
        total_quantity = 0
        for ingredient_name, quantity in self._ingredients.items():
            ingredient = self._food.get_raw_material(ingredient_name)
            total_value += get_nutritional_value(ingredient) * quantity
            total_quantity += quantity
        return total_value/total_quantity

    @property
    def name(self) -> str:
        return self._name

    @property
    def calories(self) -> float:
        return self.calculate_nutritional_value(lambda ingredient: ingredient.calories)

    @property
    def proteins(self) -> float:
        return self.calculate_nutritional_value(lambda ingredient: ingredient.proteins)

    @property
    def carbs(self) -> float:
        return self.calculate_nutritional_value(lambda ingredient: ingredient.carbs)

    @property
    def fats(self) -> float:
        return self.calculate_nutritional_value(lambda ingredient: ingredient.fats)

    @property
    def per100g(self) -> bool:
        return True

    def __repr__(self) -> str:
        string_repr = [f"{name} {quantity:3.1f}" for name, quantity in self._ingredients.items()]
        return "\n".join(string_repr)


class Menu(NutritionalElement):

    def __init__(self, name: str, food: "Food"):
        self._name = name
        self._food = food
        self._calories = 0
        self._proteins = 0
        self._carbs = 0
        self._fats = 0

    def add_recipe(self, recipe_name: str, quantity: float) -> "Menu":
        recipe = self._food.get_recipe(recipe_name)
        self._calories += recipe.calories * quantity / 100
        self._proteins += recipe.proteins * quantity / 100
        self._carbs += recipe.carbs * quantity / 100
        self._fats += recipe.fats * quantity / 100
        return self

    def add_product(self, product_name: str) -> "Menu":
        product = self._food.get_product(product_name)
        self._calories += product.calories
        self._proteins += product.proteins
        self._carbs += product.carbs
        self._fats += product.fats
        return self

    @property
    def name(self) -> str:
        return self._name

    @property
    def calories(self) -> float:
        return self._calories

    @property
    def proteins(self) -> float:
        return self._proteins

    @property
    def carbs(self) -> float:
        return self._carbs

    @property
    def fats(self) -> float:
        return self._fats

    @property
    def per100g(self) -> bool:
        return False


class RawMaterial(NutritionalElement):

    def __init__(self, name: str, calories: float, proteins: float, carbs: float, fats: float):
        self._name = name
        self._calories = calories
        self._proteins = proteins
        self._carbs = carbs
        self._fats = fats

    @property
    def name(self) -> str:
        return self._name

    @property
    def calories(self) -> float:
        return self._calories

    @property
    def proteins(self) -> float:
        return self._proteins

    @property
    def carbs(self) -> float:
        return self._carbs

    @property
    def fats(self) -> float:
        return self._fats

    @property
    def per100g(self) -> bool:
        return True


class Product(NutritionalElement):
    def __init__(self, name: str, calories: float, proteins: float, carbs: float, fats: float):
        self._name = name
        self._calories = calories
        self._proteins = proteins
        self._carbs = carbs
        self._fats = fats

    def __lt__(self, other):
        return self.name < other.name

    @property
    def name(self) -> str:
        return self._name

    @property
    def calories(self) -> float:
        return self._calories

    @property
    def proteins(self) -> float:
        return self._proteins

    @property
    def carbs(self) -> float:
        return self._carbs

    @property
    def fats(self) -> float:
        return self._fats

    @property
    def per100g(self) -> bool:
        return False

