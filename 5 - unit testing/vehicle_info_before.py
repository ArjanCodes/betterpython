class VehicleInfo:

    def __init__(self, brand, electric, catalogue_price):
        self.brand = brand
        self.electric = electric
        self.catalogue_price = catalogue_price

    # This method computes the tax payable for this particular vehicle and
    # returns that as a positive floating point value.
    # You can optionally provide an amount below which no tax is computed
    def compute_tax(self, tax_exemption_amount: int = 0) -> float:
        if tax_exemption_amount < 0:
            raise ValueError(f"tax_exemption_amount should be a positive number, but received {tax_exemption_amount} instead.")
        tax_percentage = 0.05
        if self.electric:
            tax_percentage = 0.02
        return tax_percentage * (self.catalogue_price - tax_exemption_amount)

    # you can only lease this car if the catalogue price is not more than 70% of
    # your year income; year_income should be >= 0
    def can_lease(self, year_income: int) -> bool:
        # to do
        pass

# create a vehicle info object
v = VehicleInfo("BMW", False, 10000)

# compute the tax
print(f"BMW tax: {v.compute_tax()}")
