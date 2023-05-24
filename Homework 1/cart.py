from collections import Counter, namedtuple
from copy import deepcopy
from uuid import uuid4
import regex

CatalogItem = namedtuple("CatalogItem", ["sku", "description", "price"])
InventoryItem = namedtuple("InventoryItem", ["sku", "stock"])

def validatedString(toCheck, *, maxLength=1000):
    """
    Ensures that a given value is a string with a length no greater than
    maxLength, and returns the validated string if it passes the validation.
    """

    if type(toCheck) is not str:
        raise TypeError("Value must be a string")
    if len(toCheck) > maxLength:
        raise ValueError(f'Length of value cannot be longer than {maxLength}')
    return toCheck

def validatedNumber(toCheck, *, minimum=1, maximum=float('inf')):
    """
    Ensures that a given value is either an int or float (i.e., a real 
    number) and that it exists within the given bounds. If the value
    passes the checks, it is returned.
    """

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
    """
    A class representing the ID of a customer who owns a shopping cart.
    """

    def __init__(self, id):
        self._id = CustomerID.validated(id)

    @staticmethod
    def validated(id):
        """
        Validates that a given value is a correctly formatted customer id.
        """
        if type(id) is not str:
            raise TypeError("Customer ID must be a string")
        if regex.match(r'^\p{L}{3}\d{5}\p{L}{2}-[AQ]$', id) is None:
            raise ValueError("Customer ID must be formatted correctly")
        return id

class SKU:
    """
    A wrapper class containing a stock-keeping unit, which is a unique
    identifier for every distinct item in the catalogue.
    """
    def __init__(self, code):
        self._code = SKU.validated(code)
    
    @staticmethod
    def validated(code):
        """
        Validates that a given value is a correctly formatted SKU.
        """
        if type(code) is not str:
            raise TypeError("SKU must be a string")
        if regex.match(r'^[A-Z]{3}_[A-Z]{3}_\d{2}$', code) is None:
            raise ValueError("SKU must be formatted correctly")
        return code
    
    def code(self):
        """
        Getter method for the SKU contained in this class instance.
        """
        return self._code

class Quantity:
    """
    A wrapper class for a quantity, which is any positive integer.
    """
    def __init__(self, value):
        self._value = Quantity.validated(value)

    @staticmethod
    def validated(value):
        """
        Validates that a given value is a valid quantity.
        """
        if type(value) is not int:
            raise TypeError("Value must be an integer")
        if value <= 0:
            raise ValueError("Value must be greater than 0")
        return value

    def value(self):
        """
        Getter method for the stored quantity.
        """
        return self._value

class Item:
    """
    An item in an online storefront, containing a SKU, description, and price.
    """
    def __init__(self, sku, description, price):
        self._sku = SKU.validated(sku)
        self._description = validatedString(description, maxLength=1000)
        self._price = validatedNumber(price, minimum=0.01, maximum=999999999.99)

    def sku(self):
        """
        Getter method for the item's SKU.
        """
        return self._sku
    
    def description(self):
        """
        Getter method for the item's description.
        """
        return self._description
    
    def price(self):
        """
        Getter method for the item's price.
        """
        return self._price

class Cart:
    """
    A shopping cart for an online storefront.
    """
    def __init__(self, customerId):
        self._id = uuid4()
        self._customerId = CustomerID.validated(customerId)
        self._items = Counter()

    def id(self):
        """
        Getter method for the shopping cart's unique id.
        """
        return self._id
    
    def customerId(self):
        """
        Getter method for the id of the customer to whom this cart belongs.
        """
        return self._customerId
    
    def items(self):
        """
        Getter method for the cart's current contents.
        """
        return deepcopy(self._items)
    
    def addItems(self, sku, quantity, catalogue, inventory):
        """
        Adds one or more instances of an item to the shopping cart. The item
        must exist in the given catalogue and be in stock in the given inventory.
        """
        SKU.validated(sku)
        catalogue.validateHas(sku)
        inventory.validateInStock(sku)
        Quantity.validated(quantity)
        self._items[sku] += quantity

    def removeItem(self, sku):
        """
        Removes an item from the shopping cart.
        """
        SKU.validated(sku)
        del self._items[sku]

    def updateItemQuantity(self, sku, quantity, catalogue, inventory):
        """
        Sets the quantity of an item in the shopping cart. The item must exist
        in the given catalogue and be in stock in the given inventory.
        """
        SKU.validated(sku)
        catalogue.validateHas(sku)
        inventory.validateInStock(sku)
        Quantity.validated(quantity)
        self._items[sku] = quantity

    def totalCost(self, catalogue):
        """
        Calculates the total cost of all items in the cart in the 
        given catalogue.
        """
        total = 0
        for (sku, amount_in_cart) in self._items.items():
            total += catalogue.lookup(sku).price * amount_in_cart
        return total

class Catalogue:
    """
    An index of every item in the online storefront which possesses an SKU.
    """
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
        """
        Returns an item's sku, description, and price.
        """
        return self._items[self.validateHas(sku)]
    
    def validateHas(self, sku):
        """
        Checks if an item exists in the catalogue and returns the sku if it does.
        """
        if sku not in self._items:
            raise ValueError(f'No item with SKU {sku} found in catalogue')
        return sku

class Inventory:
    """
    An inventory, which tracks the stock of each item. 
    """
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
        """
        Returns the current stock of an item.
        """
        return self._items[self.validateInStock(sku)]
    
    def removeItem(self, sku):
        """
        Removes an item from the inventory.
        """
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
        return sku