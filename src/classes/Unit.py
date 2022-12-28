from enum import Enum


class Unit(Enum):
    '''
    Unit Enumerator
    Enumerator representing the different units of measure available.
    '''
    NONE = 0,
    GRAM = 1,
    OUNCEWEIGHT = 2,
    POUND = 3,
    KILOGRAM = 4,
    MILLILITER = 5,
    TEASPOON = 6,
    TABLESPOON = 7,
    OUNCEFLUID = 8,
    CUP = 9,
    PINT = 10,
    QUART = 11,
    LITER = 12,
    GALLON = 13,
    EACH = 14,
    DOZEN = 15


class UnitType(Enum):
    '''
    Unit Type enumerator
    Enumerator representing the type of unit the Unit enumerator is.
    '''
    NONE = 0,
    WEIGHT = 1,
    VOLUME = 2,
    COUNT = 3


class UnitOfMeasure:
    '''
    Unit Of Measure class
    Unit of measure object that will be used where quantities are applied.
    '''
    unit = Unit.NONE
    unitType = UnitType.NONE

    def __init__(self):
        self.unit = Unit.NONE
        self.unitType = UnitType.NONE

    def __init__(self, unit, unitType):
        self.unit = unit
        self.unitType = unitType
