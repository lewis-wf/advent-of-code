create YEAR DAY:
    mkdir -p ./{{YEAR}}/day_{{DAY}}
    cp ./solution_template.py ./{{YEAR}}/day_{{DAY}}/solution.py

get YEAR DAY:
    ./get_data.sh {{YEAR}} {{DAY}}

all YEAR DAY:
    just create {{YEAR}} {{DAY}}
    just get {{YEAR}} {{DAY}}

# Run a given day's solution with the latest cpython
run YEAR DAY:
    uv run ./{{YEAR}}/day_{{DAY}}/solution.py

# Run a given day's solution with the latest pypy [this may be faster but is less broadly compatible]
pypy YEAR DAY:
    uv run -p pypy ./{{YEAR}}/day_{{DAY}}/solution.py