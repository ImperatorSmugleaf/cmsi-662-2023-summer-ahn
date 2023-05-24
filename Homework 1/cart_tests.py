import unittest
from cart import *

TEST_CUSTOMER_ID = 'ABC12345DE-A'
TEST_SKU_1 = 'ABC_DEF_12'
TEST_SKU_2 = 'GHI_JKL_34'
TEST_SKU_3 = 'MNO_PQR_56'
TEST_DESCRIPTION = "This is an item!"
TEST_PRICE = 3.99
TEST_CATALOGUE = Catalogue([Item(TEST_SKU_1, "Description!", 100.00), Item(TEST_SKU_2, "Another description!", 1.00)])
TEST_INVENTORY = Inventory([InventoryItem(TEST_SKU_1, 10)])

class CartTests(unittest.TestCase):
    def test_init(self):
        myCart = Cart(TEST_CUSTOMER_ID)
        self.assertEqual(myCart._customerId, TEST_CUSTOMER_ID)

    def test_ids_safety(self):
        myCart = Cart(TEST_CUSTOMER_ID)
        myId = myCart.id()
        myCustomerId = myCart.customerId()
        myId = 'a different id'
        myCustomerId = 'some different customer'
        self.assertNotEqual(myCart._id, myId)
        self.assertNotEqual(myCart._customerId, myCustomerId)

    def test_items_safety(self):
        myCart = Cart(TEST_CUSTOMER_ID)
        myItems = myCart.items()
        myItems['1234'] = 10
        self.assertNotEqual(myCart._items, myItems)

    def test_add_new_item(self):
        myCart = Cart(TEST_CUSTOMER_ID)
        myCart.addItems(TEST_SKU_1, 3, TEST_CATALOGUE, TEST_INVENTORY)
        self.assertDictEqual(myCart._items, Counter({TEST_SKU_1: 3}))

    def test_add_additional_items(self):
        myCart = Cart(TEST_CUSTOMER_ID)
        myCart.addItems(TEST_SKU_1, 3, TEST_CATALOGUE, TEST_INVENTORY)
        myCart.addItems(TEST_SKU_1, 2, TEST_CATALOGUE, TEST_INVENTORY)
        self.assertDictEqual(myCart._items, Counter({TEST_SKU_1: 5}))

    def test_remove_item(self):
        myCart = Cart(TEST_CUSTOMER_ID)
        myCart.addItems(TEST_SKU_1, 3, TEST_CATALOGUE, TEST_INVENTORY)
        myCart.removeItem(TEST_SKU_1)
        self.assertDictEqual(myCart._items, Counter())

    def test_update_item_quantity(self):
        myCart = Cart(TEST_CUSTOMER_ID)
        myCart.addItems(TEST_SKU_1, 3, TEST_CATALOGUE, TEST_INVENTORY)
        myCart.updateItemQuantity(TEST_SKU_1, 5, TEST_CATALOGUE, TEST_INVENTORY)
        self.assertDictEqual(myCart._items, Counter({TEST_SKU_1: 5}))

    def test_cannot_add_item_not_in_catalogue(self):
        with self.assertRaises(ValueError):
            myCart = Cart(TEST_CUSTOMER_ID)
            myCart.addItems(TEST_SKU_3, 3, TEST_CATALOGUE, TEST_INVENTORY)
    
    def test_cannot_add_item_not_in_inventory(self):
        with self.assertRaises(ValueError):
            myCart = Cart(TEST_CUSTOMER_ID)
            myCart.addItems(TEST_SKU_2, 3, TEST_CATALOGUE, TEST_INVENTORY)

    def test_item_total_cost(self):
        catalogueItems = set()
        catalogueItems.add(Item(TEST_SKU_1, "This is an item!", 7.99))
        catalogueItems.add(CatalogItem(TEST_SKU_2, "This is an expensive item!", 39.99))
        catalogueItems.add(Item(TEST_SKU_3, "This is a cheap item!", 0.50))
        myCatalogue = Catalogue(catalogueItems)

        inventoryItems = set()
        inventoryItems.add(InventoryItem(TEST_SKU_1, 10))
        inventoryItems.add(InventoryItem(TEST_SKU_2, 20))
        inventoryItems.add(InventoryItem(TEST_SKU_3, 30))
        myInventory = Inventory(inventoryItems)

        myCart = Cart(TEST_CUSTOMER_ID)
        myCart.addItems(TEST_SKU_1, 5, myCatalogue, myInventory)
        myCart.addItems(TEST_SKU_2, 10, myCatalogue, myInventory)
        myCart.addItems(TEST_SKU_3, 15, myCatalogue, myInventory)
        self.assertEquals(myCart.totalCost(myCatalogue), 447.35)


class CustomerIDTests(unittest.TestCase):
    def test_init(self):
        self.assertEqual(CustomerID(TEST_CUSTOMER_ID)._id, TEST_CUSTOMER_ID)
    
    def test_validated_rejects_incorrect_type(self):
        with self.assertRaises(TypeError):
            CustomerID(1)
    
    def test_validated_rejects_incorrect_format(self):
        with self.assertRaises(ValueError):
            CustomerID("This is not a valid id!")


class SKUTests(unittest.TestCase):
    def test_init(self):
        mySKU = SKU(TEST_SKU_1)
        self.assertEqual(mySKU._code, TEST_SKU_1)

    def test_validated_accepts_correct_format(self):
        self.assertEqual(SKU.validated(TEST_SKU_1), TEST_SKU_1)

    def test_validated_rejects_incorrect_type(self):
        with self.assertRaises(TypeError):
            SKU.validated(1)
    
    def test_validated_rejects_incorrect_format(self):
        with self.assertRaises(ValueError):
            SKU.validated("this is not a sku!")

    def test_sku_safety(self):
        mySKU = SKU(TEST_SKU_1)
        myCode = mySKU.code()
        myCode = 'a different sku'
        self.assertNotEqual(mySKU._code, myCode)


class QuantityTests(unittest.TestCase):
    def test_init(self):
        myQuantity = Quantity(1)
        self.assertEqual(myQuantity._value, 1)

    def test_validated_accepts_valid_number(self):
        self.assertEqual(Quantity.validated(10), 10)

    def test_validated_rejects_incorrect_type(self):
        with self.assertRaises(TypeError):
            Quantity.validated('this is not a quantity!')

    def test_validated_rejects_non_integers(self):
        with self.assertRaises(TypeError):
            Quantity.validated(10.4)

    def test_validated_rejects_negative_numbers(self):
        with self.assertRaises(ValueError):
            Quantity.validated(-1)

    def test_validated_rejects_zero(self):
        with self.assertRaises(ValueError):
            Quantity.validated(0)
    
    def test_value_safety(self):
        myQuantity = Quantity(1)
        myValue = myQuantity.value()
        myValue = 2
        self.assertNotEqual(myValue, myQuantity._value)


class ItemTests(unittest.TestCase):
    def test_init(self):
        myItem = Item(TEST_SKU_1, TEST_DESCRIPTION, TEST_PRICE)
        self.assertEqual(myItem._sku, TEST_SKU_1)
        self.assertEqual(myItem._description, TEST_DESCRIPTION)
        self.assertEqual(myItem._price, TEST_PRICE)

    def test_fields_safety(self):
        myItem = Item(TEST_SKU_1, TEST_DESCRIPTION, TEST_PRICE)
        mySKU = myItem.sku()
        myDescription = myItem.description()
        myPrice = myItem.price()
        mySKU = "this is not a sku!"
        myDescription = "this item BAD! >:("
        myPrice = 0.00
        self.assertNotEqual(myItem._sku, mySKU)
        self.assertNotEqual(myItem._description, myDescription)
        self.assertNotEqual(myItem._price, myPrice)


class ValidatedStringTests(unittest.TestCase):
    def test_rejects_incorrect_type(self):
        with self.assertRaises(TypeError):
            validatedString(1)
    
    def test_rejects_string_too_long(self):
        with self.assertRaises(ValueError):
            validatedString("This is a string!", maxLength=1)
    
    def accepts_valid_string(self):
        self.assertEquals(TEST_SKU_1, validatedString(TEST_SKU_1))


class ValidatedNumberTests(unittest.TestCase):
    def test_rejects_incorrect_type(self):
        with self.assertRaises(TypeError):
            validatedNumber("This is not a number!")

    def test_rejects_invalid_min(self):
        with self.assertRaises(TypeError):
            validatedNumber(1, minimum="This is not a number!")
    
    def test_rejects_invalid_max(self):
        with self.assertRaises(TypeError):
            validatedNumber(1, maximum="This is not a number!")

    def test_rejects_incorrect_bounds(self):
        with self.assertRaises(ValueError):
            validatedNumber(1, minimum=10, maximum=-1)

    def test_rejects_number_too_large(self):
        with self.assertRaises(ValueError):
            validatedNumber(10, maximum=9)

    def test_rejects_number_too_small(self):
        with self.assertRaises(ValueError):
            validatedNumber(-1, minimum=1)
    
    def accepts_valid_number(self):
        self.assertEquals(validatedNumber(5), 5)


class CatalogueTests(unittest.TestCase):
    def test_init(self):
        items = set()
        items.add(Item(TEST_SKU_1, "This is an item!", 7.99))
        items.add(CatalogItem(TEST_SKU_2, "This is an expensive item!", 39.99))
        items.add(Item(TEST_SKU_3, "This is a cheap item!", 0.50))
        myCatalogue = Catalogue(items)
        testItems = dict()
        testItems[TEST_SKU_1] = CatalogItem(TEST_SKU_1, "This is an item!", 7.99)
        testItems[TEST_SKU_2] = CatalogItem(TEST_SKU_2, "This is an expensive item!", 39.99)
        testItems[TEST_SKU_3] = CatalogItem(TEST_SKU_3, "This is a cheap item!", 0.50)
        self.assertDictEqual(myCatalogue._items, testItems)

    def test_rejects_invalid_type(self):
        items = set()
        items.add("This is not an item!")
        with self.assertRaises(TypeError):
            Catalogue(items)

    def test_item_safety(self):
        with self.assertRaises(AttributeError):
            items = set()
            items.add(Item(TEST_SKU_1, "This is an item!", 7.99))
            items.add(Item(TEST_SKU_2, "This is an expensive item!", 39.99))
            items.add(Item(TEST_SKU_3, "This is a cheap item!", 0.50))
            myCatalogue = Catalogue(items)
            myItem = myCatalogue.lookup(TEST_SKU_1)
            myItem.sku = "Different sku!"
    
    def test_rejects_non_iterables(self):
        with self.assertRaises(TypeError):
            Catalogue("This is not an iterable!")


class InventoryTests(unittest.TestCase):
    def test_init(self):
        items = set()
        items.add(InventoryItem(TEST_SKU_1, 1))
        items.add(InventoryItem(TEST_SKU_2, 2))
        items.add(InventoryItem(TEST_SKU_3, 3))
        myInventory = Inventory(items)
        testItems = Counter()
        testItems[TEST_SKU_1] = 1
        testItems[TEST_SKU_2] = 2
        testItems[TEST_SKU_3] = 3
        self.assertDictEqual(myInventory._items, testItems)

    def test_rejects_invalid_type(self):
        items = set()
        items.add("This is not an item!")
        with self.assertRaises(TypeError):
            Inventory(items)

    def test_item_safety(self):
        with self.assertRaises(AttributeError):
            items = set()
            items.add(InventoryItem(TEST_SKU_1, 1))
            items.add(InventoryItem(TEST_SKU_2, 2))
            items.add(InventoryItem(TEST_SKU_3, 3))
            myInventory = Inventory(items)
            myItem = myInventory.lookup(TEST_SKU_1)
            myItem.sku = "Different sku!"
    
    def test_rejects_non_iterables(self):
        with self.assertRaises(TypeError):
            Inventory("This is not an iterable!")

    def test_remove_item(self):
        items = set()
        items.add(InventoryItem(TEST_SKU_1, 1))
        items.add(InventoryItem(TEST_SKU_2, 2))
        items.add(InventoryItem(TEST_SKU_3, 3))
        myInventory = Inventory(items)
        testItems = Counter()
        testItems[TEST_SKU_1] = 1
        testItems[TEST_SKU_2] = 2
        myInventory.removeItem(TEST_SKU_3)
        self.assertDictEqual(myInventory._items, testItems)

    def test_add_new_item(self):
        items = set()
        items.add(InventoryItem(TEST_SKU_2, 2))
        items.add(InventoryItem(TEST_SKU_3, 3))
        myInventory = Inventory(items)
        myInventory.addItem(TEST_SKU_1, 5)
        testItems = Counter()
        testItems[TEST_SKU_1] = 5
        testItems[TEST_SKU_2] = 2
        testItems[TEST_SKU_3] = 3
        self.assertDictEqual(myInventory._items, testItems)

    def test_add_additional_items(self):
        items = set()
        items.add(InventoryItem(TEST_SKU_1, 1))
        items.add(InventoryItem(TEST_SKU_2, 2))
        items.add(InventoryItem(TEST_SKU_3, 3))
        myInventory = Inventory(items)
        myInventory.addItem(TEST_SKU_1, 4)
        testItems = Counter()
        testItems[TEST_SKU_1] = 5
        testItems[TEST_SKU_2] = 2
        testItems[TEST_SKU_3] = 3
        self.assertDictEqual(myInventory._items, testItems)

    def test_reject_item_subtraction_below_zero(self):
        items = set()
        items.add(InventoryItem(TEST_SKU_1, 1))
        myInventory = Inventory(items)
        with self.assertRaises(ValueError):
            myInventory.subtractItem(TEST_SKU_1, 2)

    def test_set_item_stock(self):
        items = set()
        items.add(InventoryItem(TEST_SKU_1, 1))
        myInventory = Inventory(items)
        myInventory.setItemStock(TEST_SKU_1, 5)
        self.assertEqual(myInventory.lookup(TEST_SKU_1), 5)

    def test_rejects_item_quantity_greater_than_stock(self):
        with self.assertRaises(ValueError):
            TEST_INVENTORY.validateInStock(TEST_SKU_1, 100)


if __name__ == '__main__':
    unittest.main()