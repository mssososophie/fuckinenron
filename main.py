import matplotlib.pyplot as plt
import numpy as np
import sys
import csv
import re

csv.field_size_limit(sys.maxsize)
with open('emails.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    fuck_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            if 'fuck' in row[1]:
                fuck_count += 1
            line_count += 1

    print(f'Processed {line_count} lines.')
    print(f'Found {fuck_count} fucks.')

    #Histogram

fuckdata  = [fuck_count]
plt.hist(fuck_count)
plt.show()
