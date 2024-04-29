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

pub struct VehicleRegistry;

impl VehicleRegistry {
    pub fn generate_vehicle_id(&self, length: usize) -> String {
        generate_random_string(length, false)
    }

    pub fn generate_vehicle_license(&self, id: &str) -> String {
        let front = &id[0..2];
        let middle = generate_random_string(2, true);
        let last = generate_random_string(2, false);

        format!("{front}-{middle}-{last}")
    }
}

pub struct Application;

impl Application {
    pub fn register_vehicle(&self, brand: &str) {
        // create a registry instance
        let registry = VehicleRegistry;

        // generate a vehicle id of length 12
        let vehicle_id = registry.generate_vehicle_id(12);

        // now generate a license plate for the vehicle
        // using the first two characters of the vehicle id
        let license_plate = registry.generate_vehicle_license(&vehicle_id);

        // compute the catalogue price
        let mut catalogue_price = 0;

        if brand == "Tesla Model 3" {
            catalogue_price = 60000;
        } else if brand == "Volkswagen ID3" {
            catalogue_price = 35000;
        } else if brand == "BMW 5" {
            catalogue_price = 45000;
        }

        // compute the tax percentage (default 5% of the catalogue price, except for electric cars where it is 2%)
        let mut tax_percentage = 0.05;

        if brand == "Tesla Model 3" || brand == "Volkswagen ID3" {
            tax_percentage = 0.02;
        }

        // compute the payable tax
        let payable_tax = tax_percentage * catalogue_price as f32;

        // print out the vehicle registration information
        println!("Registration complete. Vehicle information:");
        println!("Brand: {brand}");
        println!("Id: {vehicle_id}");
        println!("License plate: {license_plate}");
        println!("Payable tax: {payable_tax:?}");
    }
}