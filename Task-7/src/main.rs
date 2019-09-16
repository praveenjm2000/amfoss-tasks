extern crate regex;

use regex::Regex;
use std::io;

fn main() {
	let mut input = String::new();
	println!("Enter the email: ");
    io::stdin().read_line(&mut input)
		.ok()
        .expect("Input error");

    let re = Regex::new(r"([\w]+)@([a-z]+)mail.com").unwrap();
  
	if re.is_match(&input) {
		println!("{} is a Valid Email", input);
		}
	else {
		println!("{} is NOT A VALID EMAIL", input);
		}

}

