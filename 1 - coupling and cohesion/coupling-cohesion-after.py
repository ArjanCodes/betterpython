from enum import Enum
from dataclasses import dataclass
import random
import string

ELECTRIC_TAX = 0.02
REGULAR_TAX = 0.02


@dataclass
class VehicleInfo:
    brand_name: str
    electric: bool
    catalogue_price: float

    def print(self):
        print(f"Brand: {self.brand_name}")
        print(f"Payable tax: {self.compute_tax()}")

    def compute_tax(self):
        if self.electric:
            return ELECTRIC_TAX * self.catalogue_price
        return REGULAR_TAX * self.catalogue_price


@dataclass
class Vehicle:
    id: str
    license_plate: str
    info: VehicleInfo

    def print(self):
        print(f"Id: {self.id}")
        print(f"License plate: {self.license_plate}")
        self.info.print()


class VehicleBrands(Enum):
    BMW_5 = VehicleInfo('BMW 5', False, 45000)
    TESLA_3 = VehicleInfo('Tesla Model 3', True, 60000)
    VW_ID3 = VehicleInfo('Volkswagen ID3', True, 35000)
    TESLA_Y = VehicleInfo('Tesla Model Y', True, 75000)


def generate_vehicle_id(length: int):
    return ''.join(random.choices(string.ascii_uppercase, k=length))


def generate_vehicle_license(id: str):
    return f"{id[:2]}-{''.join(random.choices(string.digits, k=2))}-{''.join(random.choices(string.ascii_uppercase, k=2))}"


def create_vehicle(brand: VehicleBrands):
    id = generate_vehicle_id(12)
    license_plate = generate_vehicle_license(id)
    return Vehicle(id, license_plate, brand.value)


def register_vehicle(brand: VehicleBrands):
    create_vehicle(brand).print()


register_vehicle(VehicleBrands.VW_ID3)
