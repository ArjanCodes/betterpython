import unittest

class VehicleInfo:
    brand: str
    electric: bool
    catalogue_price: int

    def __init__(self, brand, electric, catalogue_price):
        self.brand = brand
        self.electric = electric
        self.catalogue_price = catalogue_price

    def compute_tax(self, tax_exemption_amount: int = 0):
        if tax_exemption_amount < 0:
            raise ValueError(f"tax_exemption_amount should be a positive number, but received {tax_exemption_amount} instead.")
        tax_percentage = 0.05
        if self.electric:
            tax_percentage = 0.02
        return tax_percentage * (max(self.catalogue_price - tax_exemption_amount, 0))
    
    def can_lease(self, year_income: int) -> bool:
        if year_income < 0:
            raise ValueError(f"year_income should be a positive number, but received {year_income} instead.")
        return self.catalogue_price <= 0.7 * year_income


class TestVehicleInfoMethods(unittest.TestCase):

    def test_compute_tax_non_electric(self):
        v = VehicleInfo("BMW", False, 10000)
        self.assertEqual(v.compute_tax(), 500)

    def test_compute_tax_electric(self):
        v = VehicleInfo("BMW", True, 10000)
        self.assertEqual(v.compute_tax(), 200)

    def test_compute_tax_exemption(self):
        v = VehicleInfo("BMW", False, 10000)
        self.assertEqual(v.compute_tax(5000), 250)
    
    def test_compute_tax_exemption_negative(self):
        v = VehicleInfo("BMW", False, 10000)
        self.assertRaises(ValueError, v.compute_tax, -5000)

    def test_compute_tax_exemption_high(self):
        v = VehicleInfo("BMW", False, 10000)
        self.assertEqual(v.compute_tax(20000), 0)

    def test_can_lease_false(self):
        v = VehicleInfo("BMW", False, 10000)
        self.assertEqual(v.can_lease(5000), False)

    def test_can_lease_true(self):
        v = VehicleInfo("BMW", False, 10000)
        self.assertEqual(v.can_lease(15000), True)

    def test_can_lease_negative_income(self):
        v = VehicleInfo("BMW", False, 10000)
        self.assertRaises(ValueError, v.can_lease, -5000)

# run the actual unittests
unittest.main()
