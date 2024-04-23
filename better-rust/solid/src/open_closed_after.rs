
pub struct Order<'a> {
    pub items: Vec<&'a str>,
    pub quantities: Vec<u32>,
    pub prices: Vec<f32>,
    pub status: &'a str,
}

impl<'a> Order<'a> {
    pub fn new() -> Self {
        Self { items: vec![], quantities: vec![], prices: vec![], status: "open" }
    }

    pub fn add_item(&mut self, name: &'a str, quantity: u32, price: f32) {
        self.items.push(name);
        self.quantities.push(quantity);
        self.prices.push(price);
    }

    pub fn total_price(&self) -> f32 {
        let mut total: f32 = 0.0;

        for (i, price) in self.prices.iter().enumerate() {
            total += self.quantities[i] as f32 * price;
        }

        total
    }
}

pub trait PaymentProcessor {
    fn pay(&self, order: &mut Order, security_code: &str);
}

pub struct DebitPaymentProcessor;

impl PaymentProcessor for DebitPaymentProcessor {
    fn pay(&self, order: &mut Order, security_code: &str) {
        println!("Processing debit payment type");
        println!("Verifying security code: {security_code}");
        order.status = "paid";
    }
}

pub struct CreditPaymentProcessor;

impl PaymentProcessor for CreditPaymentProcessor {
    fn pay(&self, order: &mut Order, security_code: &str) {
        println!("Processing credit payment type");
        println!("Verifying security code: {security_code}");
        order.status = "paid";        
    }
}
