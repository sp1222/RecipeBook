

class Recipe:
    id = int()
    name = str()
    description = str()
    tags = list()
    directions = str()
    ingredients = list()    # list of IngredientInRecipe objects.
    isIngredient = False    # indicates if this recipe should be created as an ingredient object as well.

    def __init__(self):
        self.id = int()
        self.name = str()
        self.description = str()
        self.tags = list()
        self.directions = str()
        self.ingredients = list()
        self.isIngredient = False

    def __init__(self, id, name, description, tags, directions, ingredients, isIngredient):
        self.id = id
        self.name = name
        self.description = description
        self.tags = tags
        self.directions = directions
        self.ingredients = ingredients
        self.isIngredient = isIngredient
