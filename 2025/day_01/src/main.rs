use std::fs;

fn main() {
    let START: i32 = 50;
    let DIAL_SIZE: i32 = 100;
    let TARGET: i32 = 0;

    let input = fs::read_to_string("./input.txt").unwrap();
    let lines: Vec<&str> = input.split("\n").collect();

    let mut current_p = START;
    let mut target_count: i32 = 0;

    // instruction = L|R<d=i32> where d is the distance to move in that direction. lower <- left, right -> higher
    for instruction in lines {
        let (direction, movement) = instruction.split_at(1);
        let movement_i: i32 = movement.parse().expect(&format!("Invalid movement int: {}", movement));

        current_p = match direction {
            "R" => (current_p+movement_i) % DIAL_SIZE,
            "L" => (current_p-movement_i) % DIAL_SIZE,
            &_ => panic!()
        };

        if current_p == 0 {target_count += 1}
    }

    print!("{}", target_count)
}
