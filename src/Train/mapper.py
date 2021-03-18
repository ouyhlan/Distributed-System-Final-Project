'''mapper.py'''

import sys

# input comes from STDIN
for line in sys.stdin:
    label, encod = line.strip().split('\t', 1)
    label, encod = int(label), eval(encod)

    # <label, encoding>
    print(f'{label}\t{encod}')