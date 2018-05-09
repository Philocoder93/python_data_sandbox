inputname = 'human-freedom-index.csv.13'

page = open(inputname, 'r')

strained_data = []

for line in page:
    if '#' != line[0]:
        stripped_line = line[:-8]
        split_line = stripped_line.split(',')



line_list = []

for line in strained_data:
    if '' != 


print(strained_data)
