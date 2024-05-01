mod coupling_cohesion_before;
mod coupling_cohesion_after;

fn main() {
    coupling_cohesion_before();

    coupling_cohesion_after();
}

#[macros::example]
fn coupling_cohesion_before() {
    use coupling_cohesion_before::*;

    let app = Application;

    app.register_vehicle("Volkswagen ID3");
}

#[macros::example]
fn coupling_cohesion_after() {
    use coupling_cohesion_after::*;

    let app = Application;

    app.register_vehicle("Volkswagen ID3");
}
