use std::cell::RefCell;

fn main() {
    single_responsibility_before();

    single_responsibility_after();

    open_closed();

    liskov_substitution();

    interface_segregation_before();

    interface_segregation_after();

    dependency_inversion();
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

#[macros::example]
fn interface_segregation_before() {
    use solid::interface_segregation_before::*;

    let mut order = Order::new();

    order.add_item("Keyboard", 1, 50.0);
    order.add_item("SSD", 1, 150.0);
    order.add_item("USB cable", 2, 5.0);

    println!("{}", order.total_price());
    
    let mut processor = DebitPaymentProcessor::new("2349875");
    processor.auth_sms(465839);
    processor.pay(&mut order);
}

#[macros::example]
fn interface_segregation_after() {
    use solid::interface_segregation_after::*;

    let mut order = Order::new();

    order.add_item("Keyboard", 1, 50.0);
    order.add_item("SSD", 1, 150.0);
    order.add_item("USB cable", 2, 5.0);

    println!("{}", order.total_price());
    
    let authorizer = RefCell::new(SMSAuthorizer::new());

    let processor = PaypalPaymentProcessor::new("hi@arjancodes.com", &authorizer);
    authorizer.borrow_mut().verify_code(465839);
    processor.pay(&mut order);
}

#[macros::example]
fn dependency_inversion() {
    use solid::dependency_inversion_after::*;

    let mut order = Order::new();

    order.add_item("Keyboard", 1, 50.0);
    order.add_item("SSD", 1, 150.0);
    order.add_item("USB cable", 2, 5.0);

    println!("{}", order.total_price());
    
    // let authorizer = RefCell::new(SMSAuthorizer::new());
    let authorizer = RefCell::new(AuthorizerRobot::new());

    let processor = PaypalPaymentProcessor::new("hi@arjancodes.com", &authorizer);
    // authorizer.borrow_mut().verify_code(465839);
    authorizer.borrow_mut().not_a_robot();
    processor.pay(&mut order);
}