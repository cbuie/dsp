import csv


'''
###Q6 print specified dictionary format:
'''

#helper f(x) create first, last name from name in csv:


def last_name(name):
    '''
    extract and append last name
    :param name: full name from faculty.csv
    :return : nothing
    '''
    name.append(name[0].split()[len(name[0].split()) - 1])


def name_tup(name):
    if len(name[0].split()[0]) < 3:
        x = name[0].split()[1], name[0].split()[len(name[0].split())-1]
        name.append(x)
    else:
        x = name[0].split()[0], name[0].split()[len(name[0].split())-1]
        name.append(x)


#read in csv and create dictionary:


reader = csv.reader(open('python/faculty.csv'))

l_name_dict = {}
for row in reader:
    last_name(row)
    key = row[4]
    if key in l_name_dict:
        l_name_dict[key] = [l_name_dict[key], row[:-1]]
        continue
    l_name_dict[key] = row[:-1]

#Print first 3:

for l_name in range(0,3):
    print l_name_dict.keys()[l_name],': ' ,l_name_dict[l_name_dict.keys()[l_name]]

print"\n^^^^^\n"
'''
###Q7 print specified dictionary format:
'''

reader = csv.reader(open('python/faculty.csv'))

f_l_name_dict = {}
for row in reader:
    name_tup(row)
    key = row[4]
    if key in f_l_name_dict:
        f_l_name_dict[key] = [f_l_name_dict[key], row[:-1]]
        continue
    f_l_name_dict[key] = row[:-1]

#Print first 3:

for tup_name in range(0,3):
    print f_l_name_dict.keys()[tup_name],': ' ,f_l_name_dict[f_l_name_dict.keys()[tup_name]]

print "\n^^^^^\n"


'''
###Q8 print out the dictionary key value pairs based on last name:
'''

import collections
alpha_name_dict = collections.OrderedDict(sorted(f_l_name_dict.items(),key=lambda t: t[0][1]))


#Print first 3:

for alpha_name in range(0,3):
    print alpha_name_dict.keys()[alpha_name],': ' ,alpha_name_dict[alpha_name_dict.keys()[alpha_name]]

print "\n^^^^^\n"
