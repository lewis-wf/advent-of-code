use std::{fs, str::FromStr};

fn main() {
    let START: i32 = 50;
    let DIAL_SIZE: i32 = 100;

    let input = fs::read_to_string("./input.txt").unwrap();
//     let input = String::from_str("L68
// L30
// R48
// L5
// R60
// L55
// L1
// L99
// R14
// L82").unwrap();

    let lines: Vec<&str> = input.split("\n").collect();

    let mut current_p = START;
    let mut target_count: i32 = 0;

    // instruction = L|R<d=i32> where d is the distance to move in that direction. lower <- left, right -> higher
    for instruction in lines {
        let (direction, movement) = instruction.split_at(1);
        let movement_i: i32 = movement
            .parse()
            .expect(&format!("Invalid movement int: {}", movement));

        let rot_value = match direction {
            "R" => current_p + movement_i,
            "L" => current_p - movement_i,
            &_ => panic!(),
        };

        if rot_value < 0 && current_p != 0 { target_count += 1; }

        let processed_value = rot_value.abs(); 

        let hits = (processed_value / DIAL_SIZE);
        println!("{} {} {} {}", instruction, current_p, rot_value, hits);
        target_count += hits;

        if processed_value == 0 {
            target_count += 1
        }

        // use mod to the new value
        current_p = rot_value.rem_euclid(DIAL_SIZE);
        
        println!("{} {}", current_p, target_count);
    }

    println!("{}", target_count)
}
