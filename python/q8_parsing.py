#The football.csv file contains the results from the English Premier League. 
# The columns labeled ‘Goals’ and ‘Goals Allowed’ contain the total number of 
# goals scored for and against each team in that season (so Arsenal scored 79 goals 
# against opponents, and had 36 goals scored against them). Write a program to read the file, 
# then print the name of the team with the smallest difference in ‘for’ and ‘against’ goals.

# The below skeleton is optional.  You can use it or you can write the script with an approach of your choice.


# import pandas
import pandas as pd

# read football.csv data
data = pd.read_csv('football.csv')

# get min score difference between 'Goals' and 'Goals Allowed'
# by creating adding a new column "Goals Difference' equalling
# the absolute value of the difference between 'Goals' and 'Goals Allowed' 
data['Goals Difference'] = abs(data['Goals'] - data['Goals Allowed'])

# determine minimum number of 'Goals Difference'
min_num_goals = data['Goals Difference'].min()

# Check for multiple 'Teams' with lowest 'Goals Difference'
count = 0 
for i in data['Goals Difference']:
    if i == min_num_goals:
        count += 1
# print result
if count > 1:
    print str(count) + " teams share the smallest difference in 'for' and 'against' goals:"
    print data.ix[data['Goals Difference']==1]['Team']
else:
    print data.iloc[data['Goals Difference'].idxmin()]["Team"] + " has the smallest difference in 'for' and 'against' goals, with " + str(min_num_goals)



