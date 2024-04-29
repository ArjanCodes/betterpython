use std::collections::HashMap;
use rand::{self, Rng};

fn generate_random_string(length: usize, digits: bool) -> String {
    rand::thread_rng()
        .sample_iter(rand::distributions::Alphanumeric)
        .map(char::from)
        .filter(|c| if digits { c.is_digit(10) } else { !c.is_digit(10) })
        .map(|c| c.to_ascii_uppercase())
        .take(length)
        .collect()
}

#[derive(Clone)]
pub struct VehicleInfo {
    pub brand: String,
    pub electric: bool,
    pub catalogue_price: u32,
}

impl VehicleInfo {
    pub fn new(brand: &str, electric: bool, catalogue_price: u32) -> Self {
        Self { brand: brand.to_string(), electric, catalogue_price }
    }

    pub fn compute_tax(&self) -> f32 {
        let mut tax_percentage = 0.05;
        if self.electric {
            tax_percentage = 0.02;
        }
        
        tax_percentage * self.catalogue_price as f32
    }

    pub fn print(&self) {
        println!("Brand: {}", self.brand);
        println!("Payable tax: {:#?}", self.compute_tax());
    }
}

pub struct Vehicle {
    pub id: String,
    pub license_plate: String,
    pub info: VehicleInfo,
}

impl Vehicle {
    pub fn new(id: &str, license_plate: String, info: VehicleInfo) -> Self {
        Self { id: id.to_string(), license_plate, info }
    }

    pub fn print(&self) {
        println!("Registration complete. Vehicle information:");
        println!("Id: {}", self.id);
        println!("License plate: {}", self.license_plate);
        self.info.print();
    }
}
pub struct VehicleRegistry {
    pub vehicle_info: HashMap<String, VehicleInfo>,
}

impl VehicleRegistry {
    pub fn new() -> Self {
        let mut vehicle_registry = Self { vehicle_info: HashMap::new() };

        vehicle_registry.add_vehicle_info("Tesla Model 3", true, 60000);
        vehicle_registry.add_vehicle_info("Volkswagen ID3", true, 35000);
        vehicle_registry.add_vehicle_info("BMW 5", false, 45000);
        vehicle_registry.add_vehicle_info("Tesla Model Y", true, 75000);

        vehicle_registry
    }

    fn add_vehicle_info(&mut self, brand: &str, electric: bool, catalogue_price: u32) {
        self.vehicle_info.insert(brand.to_string(), VehicleInfo::new(brand, electric, catalogue_price));
    }

    pub fn generate_vehicle_id(&self, length: usize) -> String {
        generate_random_string(length, false)
    }

    pub fn generate_vehicle_license(&self, id: &str) -> String {
        let front = &id[0..2];
        let middle = generate_random_string(2, true);
        let last = generate_random_string(2, false);

        format!("{front}-{middle}-{last}")
    }

    pub fn create_vehicle(&self, brand: &str) -> Vehicle {
        let id = self.generate_vehicle_id(12);
        let license_plate = self.generate_vehicle_license(&id);

        Vehicle::new(&id, license_plate, self.vehicle_info.get(brand).unwrap().clone())
    }
}

pub struct Application;

impl Application {
    pub fn register_vehicle(&self, brand: &str) {
    // create a registry instance
    let registry = VehicleRegistry::new();

    let vehicle = registry.create_vehicle(brand);

    // print out the vehicle information
    vehicle.print();
    }
}