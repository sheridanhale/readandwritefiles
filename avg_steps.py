import csv

infile = open('steps.csv','r')

csvfile = csv.reader(infile, delimiter = ',')

outfile = open('avg_steps.csv','w') 

next(csvfile)

months = ['O','January','February','March','April','May','June','July','August','September','October','November','December']

month = 1
steps_taken = 0
day_count = 0

for row in csvfile:
    if row[0] == str(month):
        steps_taken += int(row[1])
        day_count += 1
    
    else:
        avg_steps = format(steps_taken/day_count, '.2f')
        outfile.write(months[int(month)] + ', ' + str(avg_steps) + '\n')
        month = row[0]
        steps_taken = int(row[1])
        day_count = 1

avg_steps = format(steps_taken/day_count, '.2f')
outfile.write(months[int(month)] + ', ' + str(avg_steps) + '\n')
month = row[0]
steps_taken = int(row[1])
day_count = 1

outfile.close()