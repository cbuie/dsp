# The football.csv file contains the results from the English Premier League. 
# The columns labeled ‘Goals’ and ‘Goals Allowed’ contain the total number of 
# goals scored for and against each team in that season (so Arsenal scored 79 goals 
# against opponents, and had 36 goals scored against them). Write a program to read the file, 
# then print the name of the team with the smallest difference in ‘for’ and ‘against’ goals.


def load_mydata (fin,feature):
    import csv
    reader = csv.DictReader(open(fin))
    r = {}
    for row in reader:
        key = row.pop(feature)
        if key in r:
            # implement your duplicate row handling here
            pass
        r[key] = row
    return r


def find_min(data,f1,f2):
    ml = []
    for i in data:
        x = i, int(data[i]['Goals']) - int(data[i]['Goals Allowed'])
        ml.append(x)
    ml = sorted(ml, key=lambda tup: tup[1])
    return ml[0]


data = load_mydata('python/football.csv','Team')
result = find_min(data,'Goals','Goals Allowed')
print result