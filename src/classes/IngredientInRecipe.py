from Ingredient import Ingredient
from Unit import UnitOfMeasure


class IngredientInRecipe:
    ingredient = Ingredient()
    quantity = float()
    uom = UnitOfMeasure()

    def __init__(self):
        self.ingredient = Ingredient()
        self.quantity = float()
        self.uom = UnitOfMeasure()
