fn main() {
    single_responsibility_before();

    single_responsibility_after();

    open_closed();

    liskov_substitution();
}

#[macros::example]
fn single_responsibility_before() {
    use solid::single_responsibility_before::*;

    let mut order = Order::new();

    order.add_item("Keyboard", 1, 50.0);
    order.add_item("SSD", 1, 150.0);
    order.add_item("USB cable", 2, 5.0);

    println!("{}", order.total_price());
    order.pay("debit", "0372846");
}

#[macros::example]
fn single_responsibility_after() {
    use solid::single_responsibility_after::*;

    let mut order = Order::new();

    order.add_item("Keyboard", 1, 50.0);
    order.add_item("SSD", 1, 150.0);
    order.add_item("USB cable", 2, 5.0);

    println!("{}", order.total_price());
    
    let processor = PaymentProcessor {};

    processor.pay_debit(&mut order, "0372846");
}

#[macros::example]
fn open_closed() {
    use solid::open_closed_after::*;

    let mut order = Order::new();

    order.add_item("Keyboard", 1, 50.0);
    order.add_item("SSD", 1, 150.0);
    order.add_item("USB cable", 2, 5.0);

    println!("{}", order.total_price());
    
    let processor = DebitPaymentProcessor {};

    processor.pay(&mut order, "0372846");
}

#[macros::example]
fn liskov_substitution() {
    use solid::liskov_substitution_after::*;

    let mut order = Order::new();

    order.add_item("Keyboard", 1, 50.0);
    order.add_item("SSD", 1, 150.0);
    order.add_item("USB cable", 2, 5.0);

    println!("{}", order.total_price());
    
    let processor = PaypalPaymentProcessor::new("hi@arjancodes.com");

    processor.pay(&mut order);
}