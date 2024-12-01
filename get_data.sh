#!/bin/bash

BASE_URL="https://adventofcode.com"

YEAR=$1
DAY=$2

# Check values are valid
if [ -z "$YEAR" ] || [ -z "$DAY" ]; then
    echo "Error, invalid args.
    > Usage: <year> <day>"
    # Don't exit, just return
    return
fi

# Left pad day with 0 if needed
DAY=$(printf "%02d" $DAY)
# Strip leading 0s for URL
URL_DAY=$(echo $DAY | sed 's/^0*//')

# Get the input
curl -b session=$(cat ./session.txt) $BASE_URL/$YEAR/day/$URL_DAY/input > ./$YEAR/day_$DAY/input.txt
