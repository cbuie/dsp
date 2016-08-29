import pandas as pd
import csv


fout='/PycharmProjects/dsp/python/emails.csv'


headers = ['name', 'degree', 'title', 'email']
data = pd.read_csv('python/faculty.csv', header=0, names=headers)
email_list = list(data['email'])


with open(fout, 'wb') as myfile:
    for e in email_list:
        csv.writer(myfile).writerow([e])

