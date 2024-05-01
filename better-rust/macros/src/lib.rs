use proc_macro::TokenStream;
use quote::quote;
use syn;

#[proc_macro_attribute]
pub fn example(_attr: TokenStream, item: TokenStream) -> TokenStream {
    let input = syn::parse_macro_input!(item as syn::ItemFn);
    let ident = input.sig.ident;
    let name = ident.clone().to_string();
    let block = input.block;

    let gen = quote! {
        fn #ident() {
            println!("running `{}`:\n", #name);
            #block;
            println!("-------------\n");
        }
    };

    gen.into()
}