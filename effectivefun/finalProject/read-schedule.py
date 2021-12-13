import csv

schedule = []

with open('schedule.csv') as f:
    reader = csv.reader(f)
    schedule = list(reader)

print(schedule)