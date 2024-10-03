from Inventory import *
import unittest


class Test_inventory(unittest.TestCase):
    def setUp(self):
        self.inventory = Inventory()
        self.inventory.add_new_item(1, "Milk", 300, 50)
        self.inventory.add_new_item(2, "Bread", 100, 70)
        self.inventory.add_new_item(3, "Eggs", 90, 80)

    def test_add_new_item(self):
        self.inventory.add_new_item(4, "Juice", 80, 80)
        self.assertIn(4, self.inventory.item)
        self.assertEqual(self.inventory.item[4].name, "Juice")
        self.assertEqual(self.inventory.item[4].quantity, 80)

    def test_update_item(self):
        self.inventory.update_item(1, 20)
        self.assertEqual(self.inventory.item[1].quantity, 70)

    def test_remove_item(self):
        self.inventory.remove_item(4)
        self.assertNotIn(4, self.inventory.item)

    def test_display_whole_inventory(self):
        self.inventory.display()

    def test_check_stock(self):
        self.inventory.check_stock(4, "Juice", 80)
        self.inventory.check_stock(2, "Bread", 70)

    def test_track_sales_record(self):
        self.inventory.track_sales(3, 10)
        self.assertEqual(self.inventory.item[3].quantity, 70)
        self.inventory.track_sales(3, 70)

    def test_report_of_inventory(self):
        self.inventory.report(300, 50)


if __name__ == "__main__":
    unittest.main()
