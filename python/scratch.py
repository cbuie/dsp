import pandas as pd

headers = ['name', 'degree', 'title', 'email']
data = pd.read_csv('python/faculty.csv', header=0, names=headers)


#Q1 print unique degrees and frequencies:
data.degree = data.degree.str.replace('.', '')
degree_str = " ".join(data.degree)
degree_cl = pd.Series(degree_str.split())
degree_fr = degree_cl.groupby(degree_cl).count()
print degree_fr
print '\n^^^^^\n'


#Q2 print unique titles and frequencies:
data.title = data.title.str.replace(' is ', ' of ')
title_gb = data.groupby('title')
print title_gb.size()
print '\n^^^^^\n'


#Q3 print a list of emal addresses:

email_list = list(data['email'])
print(list(email_list))
print '\n^^^^^\n'


#Q4 Print unique email domains:

domain_list = []
for i in email_list:
    domain_list.append(i.split('@')[1])
domain_set = set(domain_list)
print domain_set # unique domain set
print '\n^^^^^\n'


#Q5 write emails to csv:
import csv

fout='/Users/chrisbuie/PycharmProjects/dsp/python/emails.csv'

with open(fout, 'wb') as myfile:
    for e in email_list:
        csv.writer(myfile).writerow([e])

#part III dictionary:


import csv

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


#Q6 print specified dictionary format:

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

print l_name_dict['Ellenberg']
print l_name_dict['Xie']

for l_name in range(0,3):
    print l_name_dict.keys()[l_name],' : ' ,l_name_dict[l_name_dict.keys()[l_name]]


# >>> # dictionary sorted by key
import collections
d = {'banana': 3, 'apple':4, 'pear': 1, 'orange': 2}
collections.OrderedDict(sorted(d.(), key=lambda t: t[1]))
#OrderedDict([('apple', 4), ('banana', 3), ('orange', 2), ('pear', 1)])

'''

faculty_dict = { 'Ellenberg': [['Ph.D.', 'Professor', 'sellenbe@upenn.edu'], ['Ph.D.', 'Professor', 'jellenbe@mail.med.upenn.edu']],
              'Li': [['Ph.D.', 'Assistant Professor', 'liy3@email.chop.edu'], ['Ph.D.', 'Associate Professor', 'mingyao@mail.med.upenn.edu'], ['Ph.D.', 'Professor', 'hongzhe@upenn.edu']]}

'''

#
# def name_tup():
#     for name in result.keys():
#         if len(tuple(name.split())[0]) < 3:
#             x = tuple(name.split())[1], tuple(name.split())[len(tuple(name.split()))-1]
#             result[name].append(x)
#         else:
#             x = tuple(name.split())[0], tuple(name.split())[len(tuple(name.split())) - 1]
#             result[name].append(x)
#     return result
#
# new_dict = name_tup()
# print new_dict
#
# dict = dict.fromkeys(new_keys,result.values())
