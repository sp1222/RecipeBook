
class Ingredient:
    __slots__ = 'id', 'name', 'description', 'tags'

    def __init__(self):
        self.id = -1
        self.name = str()
        self.description = str()
        self.tags = set()

    def __init__(self, id, name, description, tags):
        self.id = id
        self.name = name
        self.description = description
        self.tags = tags
