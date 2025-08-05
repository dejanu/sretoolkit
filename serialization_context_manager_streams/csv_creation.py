#!/usr/bin/env python3

import csv

def print_csv(filename):
    with open(filename,'r') as f:
        line_count = 0
        reader = csv.reader(f, delimiter=',', quotechar='"')
        # column is line_count == 0
        for row in reader:
            if line_count == 0:
                print(f"Column are {' '.join(row)}")
                line_count += 1
            else:
                if row:  # Check if row is not empty
                    line_count += 1
                    print(row)
        print(f"Processed {line_count} lines.")

if __name__ == "__main__":
    # read using csv dict reader (columns are the keys)
    d = {}
    with open('rsvp.csv', 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            d[row.get('name')] = {k:v for k,v in row.items() if k != 'name'}
    print(d)
