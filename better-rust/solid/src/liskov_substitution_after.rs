
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
    fn pay(&self, order: &mut Order);
}

pub struct DebitPaymentProcessor<'a> {
    pub security_code: &'a str,
}

impl<'a> DebitPaymentProcessor<'a> {
    pub fn new(security_code: &'a str) -> Self {
        Self { security_code }
    }
}

impl PaymentProcessor for DebitPaymentProcessor<'_> {
    fn pay(&self, order: &mut Order) {
        println!("Processing debit payment type");
        println!("Verifying security code: {}", {self.security_code});
        order.status = "paid";
    }
}

pub struct CreditPaymentProcessor<'a> {
    pub security_code: &'a str, 
}

impl<'a> CreditPaymentProcessor<'a> {
    pub fn new(security_code: &'a str) -> Self {
        Self { security_code }
    }
}

impl PaymentProcessor for CreditPaymentProcessor<'_> {
    fn pay(&self, order: &mut Order) {
        println!("Processing credit payment type");
        println!("Verifying security code: {}", {self.security_code});
        order.status = "paid";        
    }
}

pub struct PaypalPaymentProcessor<'a> {
    pub email_address: &'a str,
}

impl<'a> PaypalPaymentProcessor<'a> {
    pub fn new(email_address: &'a str) -> Self {
        Self { email_address }
    }
}

impl PaymentProcessor for PaypalPaymentProcessor<'_> {
    fn pay(&self, order: &mut Order) {
        println!("Processing paypal payment type");
        println!("Using email address: {}", {self.email_address});
        order.status = "paid";        
    }
}
