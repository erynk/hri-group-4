import sys
import csv

schedule = sys.argv[1]

schedule = schedule.split(',')

with open('schedule.csv', 'w') as f:
    write = csv.writer(f)
    write.writerow(schedule)

print(schedule)