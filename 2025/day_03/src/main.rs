use core::num;
use std::{fs, str::FromStr};

fn concat_ints(left: u32, right: u32) -> u32 {
    let digits = right.checked_ilog10().unwrap() + 1;
    let pow10 = 10u32.pow(digits);
    left * pow10 + right
}

fn main() {
    let input = fs::read_to_string("./input.txt").unwrap();
//     let input = String::from_str(
//         "987654321111111
// 811111111111119
// 234234234234278
// 818181911112111",
//     )
//     .unwrap();

    let lines: Vec<&str> = input.split("\n").collect();

    let mut target_sum = 0;

    for line in lines {
        // index, value
        let mut left_large = 0;
        let mut right_large = 0;

        let chars = line.chars();
        let chars_v: Vec<_> = chars.clone().collect();
        let chars_end = chars_v.len() - 1;

        for (index, char) in chars.enumerate() {
            let num_char = char.to_digit(10).unwrap();

            if index == chars_end {
                if num_char > right_large {
                    right_large = num_char
                }
            } else if num_char > left_large {
                left_large = num_char;
                right_large = 0
            } else if num_char > right_large {
                right_large = num_char
            }
        }

        println!(
            "{} {:?} {:?} {}",
            line,
            left_large,
            right_large,
            concat_ints(left_large, right_large)
        );
        target_sum += concat_ints(left_large, right_large);
    }
    println!("{}", target_sum)
}
