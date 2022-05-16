from diet.nutritional import NutritionalElement


class Recipe(NutritionalElement):

    def add_ingredient(self, raw_material_name: str, quantity: float) -> "Recipe":
        pass

    @property
    def name(self) -> str:
        pass

    @property
    def calories(self) -> float:
        pass

    @property
    def proteins(self) -> float:
        pass

    @property
    def carbs(self) -> float:
        pass

    @property
    def fats(self) -> float:
        pass

    @property
    def per100g(self) -> bool:
        pass

    def __repr__(self) -> str:
        pass


class Menu(NutritionalElement):

    def add_recipe(self, recipe_name: str, quantity: float) -> "Menu":
        pass

    def add_product(self, product_name: str) -> "Menu":
        pass

    @property
    def name(self) -> str:
        pass

    @property
    def calories(self) -> float:
        pass

    @property
    def proteins(self) -> float:
        pass

    @property
    def carbs(self) -> float:
        pass

    @property
    def fats(self) -> float:
        pass

    @property
    def per100g(self) -> bool:
        pass
