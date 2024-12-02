create YEAR DAY:
    mkdir -p ./{{YEAR}}/day_{{DAY}}
    touch ./{{YEAR}}/day_{{DAY}}/solution.py
    echo 'from aoc_tools import *\n\ninput = get_input_file("{{YEAR}}/day_{{DAY}}/")' > ./{{YEAR}}/day_{{DAY}}/solution.py

get YEAR DAY:
    ./get_data.sh {{YEAR}} {{DAY}}
    