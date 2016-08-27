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

