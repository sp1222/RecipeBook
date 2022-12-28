
class Ingredient:
    id = int()
    name = str()
    description = str()
    tags = set()

    def __init__(self):
        self.id = -1

    def __init__(self, id, name, description, tags):
        self.id = id
        self.name = name
        self.tags = tags
