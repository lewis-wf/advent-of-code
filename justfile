create YEAR DAY:
    mkdir -p ./{{YEAR}}/day_{{DAY}}
    cp ./solution_template.py ./{{YEAR}}/day_{{DAY}}/solution.py

get YEAR DAY:
    ./get_data.sh {{YEAR}} {{DAY}}
    