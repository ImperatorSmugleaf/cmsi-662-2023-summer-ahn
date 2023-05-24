from collections import Counter, namedtuple
from copy import deepcopy
from uuid import uuid4
import regex

CatalogItem = namedtuple("CatalogItem", ["sku", "description", "price"])
InventoryItem = namedtuple("InventoryItem", ["sku", "stock"])

def validatedString(toCheck, *, maxLength=1000):
    if type(toCheck) is not str:
        raise TypeError("Value must be a string")
    if len(toCheck) > maxLength:
        raise ValueError(f'Length of value cannot be longer than {maxLength}')
    return toCheck

def validatedNumber(toCheck, *, minimum=1, maximum=float('inf')):
    if type(toCheck) is not int and type(toCheck) is not float:
        raise TypeError("Value must be a real number")
    if type(minimum) is not int and type(minimum) is not float:
        raise TypeError("Minimum must be a real number")
    if type(maximum) is not int and type(maximum) is not float:
        raise TypeError("Maximum must be a real number")
    if maximum < minimum:
        raise ValueError("Minimum must be less than maximum")
    if toCheck < minimum:
        raise ValueError(f'Value cannot be any less than {minimum}')
    if toCheck > maximum:
        raise ValueError(f'Value cannot be greater than {maximum}')
    return toCheck

class CustomerID:
    def __init__(self, id):
        self._id = CustomerID.validated(id)

    @staticmethod
    def validated(id):
        if type(id) is not str:
            raise TypeError("Customer ID must be a string")
        if regex.match(r'^\p{L}{3}\d{5}\p{L}{2}-[AQ]$', id) is None:
            raise ValueError("Customer ID must be formatted correctly")
        return id

class SKU:
    def __init__(self, code):
        self._code = SKU.validated(code)
    
    @staticmethod
    def validated(code):
        if type(code) is not str:
            raise TypeError("SKU must be a string")
        if regex.match(r'^[A-Z]{3}_[A-Z]{3}_\d{2}$', code) is None:
            raise ValueError("SKU must be formatted correctly")
        return code
    
    def code(self):
        return self._code

class Quantity:
    def __init__(self, value):
        self._value = Quantity.validated(value)

    @staticmethod
    def validated(value):
        if type(value) is not int:
            raise TypeError("Value must be an integer")
        if value <= 0:
            raise ValueError("Value must be greater than 0")
        return value

    def value(self):
        return self._value

class Item:
    def __init__(self, sku, description, price):
        self._sku = SKU.validated(sku)
        self._description = validatedString(description, maxLength=1000)
        self._price = validatedNumber(price, minimum=0.01, maximum=999999999.99)

    def sku(self):
        return self._sku
    
    def description(self):
        return self._description
    
    def price(self):
        return self._price

class Cart:
    def __init__(self, customerId):
        self._id = uuid4()
        self._customerId = CustomerID.validated(customerId)
        self._items = Counter()

    def id(self):
        return self._id
    
    def customerId(self):
        return self._customerId
    
    def items(self):
        return deepcopy(self._items)
    
    def addItems(self, sku, quantity, catalogue, inventory):
        SKU.validated(sku)
        catalogue.validateHas(sku)
        inventory.validateInStock(sku)
        Quantity.validated(quantity)
        self._items[sku] += quantity

    def removeItem(self, sku):
        SKU.validated(sku)
        del self._items[sku]

    def updateItemQuantity(self, sku, quantity, catalogue, inventory):
        SKU.validated(sku)
        catalogue.validateHas(sku)
        inventory.validateInStock(sku)
        Quantity.validated(quantity)
        self._items[sku] = quantity

    def totalCost(self, catalogue):
        total = 0
        for (sku, amount_in_cart) in self._items.items():
            total += catalogue.lookup(sku).price * amount_in_cart
        return total

class Catalogue:
    def __init__(self, items):
        self._items = dict()
        try:
            iter(items)
        except:
            raise TypeError("Expected iterable")
        for item in items:
            if type(item) is Item:
                self._items[item.sku()] = CatalogItem(item.sku(), item.description(), item.price())
            elif type(item) is CatalogItem:
                self._items[item.sku] = CatalogItem(item.sku, item.description, item.price)
            else:
                raise TypeError("Item or CatalogItem type expected")

    def lookup(self, sku):
        return self._items[sku]
    
    def validateHas(self, sku):
        if sku not in self._items:
            raise ValueError(f'No item with SKU {sku} found in catalogue')

class Inventory:
    def __init__(self, items):
        self._items = Counter()
        try:
            iter(items)
        except:
            raise TypeError("Expected iterable")
        for item in items:
            if type(item) is not InventoryItem:
                raise TypeError("InventoryItem type expected")
            self._items[SKU.validated(item.sku)] = Quantity.validated(item.stock)

    def lookup(self, sku):
        return self._items[sku]
    
    def removeItem(self, sku):
        del self._items[sku]

    def addItem(self, sku, quantity):
        self._items[SKU.validated(sku)] += Quantity.validated(quantity)

    def subtractItem(self, sku, quantity):
        if Quantity.validated(quantity) > self._items[SKU.validated(sku)]:
            raise ValueError("Cannot subtract quantity from item greater than current stock")
        self._items[sku] -= quantity

    def setItemStock(self, sku, quantity):
        self._items[SKU.validated(sku)] = Quantity.validated(quantity)

    def validateInStock(self, sku, quantity=1):
        if not (sku in self._items and self._items[sku] != 0):
            raise ValueError("Item not in stock")
        if self._items[sku] < Quantity.validated(quantity):
            raise ValueError("Requested quantity greater than stock")