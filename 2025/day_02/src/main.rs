use std::{collections::btree_map::Range, fs, str::FromStr};

fn main() {
    let input = fs::read_to_string("./input.txt").unwrap();
    // let input = String::from_str("11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124").unwrap();
    let raw_ranges: Vec<&str> = input.split(",").collect();

    // Parse the range ints
    let parse_range = |raw: &&str| -> (u64, u64) {
        let parts: Vec<&str> = raw.split("-").collect();

        if parts.len() != 2 {
            panic!("Length of parts does not equal 2!")
        }

        let left: u64 = parts[0]
            .parse()
            .expect("Invalid left part int");
        let right: u64 = parts[1].parse().expect("Invalid right part int");

        (left, right)
    };

    let ranges = raw_ranges.iter().map(parse_range);

    // Now, we need to iterate over all the values in each of the ranges
    // this is very expensive, yippee
    let mut target_sum = 0;
    for range in ranges {
        for num in range.0..(range.1+1) {
            let num_str = num.to_string();
            let num_parts = num_str.split_at(num_str.len()/2);
            
            // Now do the parts comparison
            if num_parts.0 == num_parts.1 {
                target_sum += num
            }
        }
    }
    println!("{:?}", target_sum)
}
