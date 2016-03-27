# Advanced Python 
# Part 1 - Regular Expressions

import re
import pandas as pd

# read data 
url = "https://raw.githubusercontent.com/Napenthy/dsp/master/python/faculty.csv"
df = pd.read_csv(url)


# Q1. Find how many different degrees there are, and their frequencies: Ex: PhD, ScD, MD, MPH, BSEd, MS, JD, etc.

#remove white spaces and '.' from 'degree' column
df[' degree'] = df[' degree'].map(lambda x: x.lstrip().replace('.', ''))
df[' degree'] = df[' degree'].str.replace('[^\w\s]','')

# degree types (I'd like to automate this process)

# Print results
print 
print 'Q1. Different degree types and frequency of each:'
print
print 'Ph.D.s:   ', df[' degree'].str.contains(r'PhD').sum()
print 'Sc.D.s:   ', df[' degree'].str.contains(r'ScD').sum()
print 'MPHs:     ', df[' degree'].str.contains(r'MPH').sum()
print 'MSs:      ', df[' degree'].str.contains(r'MS').sum()
print 'MDs:      ', df[' degree'].str.contains(r'MD').sum()
print 'B.S.Ed.s: ', df[' degree'].str.contains(r'BSEd').sum()
print 'JDs:      ', df[' degree'].str.contains(r'JD').sum()
print 'MAs:      ', df[' degree'].str.contains(r'MA').sum()


# Q2. Find how many different titles there are, and their frequencies: Ex: Assistant Professor, Professor
# Clean data; replace 'is' with 'of'
df[' title'] = df[' title'].str.replace('is','of')
print
print 'Q2. Different titles and the frequency of each:'
print
print df[' title'].value_counts() # I'd like to find a way to not print 'dtype: int64'


# Q3. Search for email addresses and put them in a list. Print the list of email addresses.
print
print 'Q3. List of emails'
print
email = list(df[' email'])
print email


# Q4. Find how many different email domains there are (Ex: mail.med.upenn.edu, upenn.edu, email.chop.edu, etc.). Print the list of unique email domains.
emails = df[' email']
domains = []
for e in emails:
    domains += re.findall(r'@(.*)', e)
print
print 'Q4. Domain types'
print
print "There are {} different email domains.".format(len(list(set(domains))))
print list(set(domains))
