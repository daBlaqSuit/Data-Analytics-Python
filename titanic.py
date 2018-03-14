# -*- coding: utf-8 -*-
"""
Created on Sat Feb 17 14:28:34 2018

@author: Thabang I. Phefo
@company: PBTGroup Academy
@Date: 19 / 02 / 2018

This is a Final Project from the Udacity 'Intro into Data Analysis' Course and 
submitted to the PBTGroup Academy. Due to the nature of the dataset that I chose, 
it only allowed me to perform the following functions based on
the questions I asked, and they were answered using the data. Should more questions arise,
they can be easily answered
"""

# Import libraries needed to be used
""" """

import pandas as pd
from pandas import DataFrame
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

titanic_data = 'titanic_data.csv'

data_set = pd.read_csv(titanic_data)



print 'The Titanic Story using the Titanic Data Set provided, Please enjoy:\nTitanic :'
passengers = data_set['PassengerId'].max() #number of passengers on the ship
male_passengers = len(data_set.loc[(data_set['Sex'] == 'male')])
female_passengers = len(data_set.loc[(data_set['Sex'] == 'female')])
children = len(data_set.loc[(data_set['Age'] <= 17)])
p_died = len(data_set.loc[(data_set['Survived'] == 0)])
p_survived = len(data_set.loc[(data_set['Survived'] == 1)])
tot_fare = np.round(data_set['Fare'].sum(),3)
child_deaths = len(data_set.loc[(data_set['Age'] <= 17) & (data_set['Survived'] == 0)])
f_survived = len(data_set.loc[(data_set['Sex'] == 'female') & (data_set['Survived'] == 1)])
f_deaths = len(data_set.loc[(data_set['Sex'] == 'female') & (data_set['Survived'] == 0)])
m_survived = len(data_set.loc[(data_set['Sex'] == 'male') & (data_set['Survived'] == 1)])
m_deaths = len(data_set.loc[(data_set['Sex'] == 'male') & (data_set['Survived'] == 0)])
families_num = len(data_set.loc[(data_set['SibSp'] > 0)])

#Uncomment to see the names of people who were on the Titanic ship
#names = data_set['Name']
#print 'These are the names of people who were on the ship:',names


ratio_m_to_f = (male_passengers/female_passengers)
print 'The ratio of Men to Woman is:',ratio_m_to_f
print 'Survived females:',f_survived
print 'Female deaths:',f_deaths
print 'Survived males:',m_survived
print 'Male deaths:',m_deaths

print

print 'RMS Titanic was a British passenger liner that sank in the North Atlantic Ocean\
 in the early morning hours of 15 April 1912, after it collided with an iceberg during its maiden voyage\
 from Southampton to New York City.\n'
print 'The Titanic had {} Passengers onboard. There were {} Male and {} Female Passengers on the ship of \
which {} were children of under the age of 17. It was an unfortunate tragic when {} passengers died \
and only {} survived. So many people lost their families, their loved ones, {} children died.\
 A total of {} dollars was paid. About {} passengers were with thier familes.\
'.format(passengers,male_passengers,female_passengers, children,p_died, p_survived,child_deaths,tot_fare, families_num)
print '\nAlthough the largest and strongest ship ever made at the time fell, they could not save all due to the number of \
life boats not enough to accomodate all the passengers. The survivors were mostly woman and this shows women\
took priority during the assembling of life boats while men stayed behind as most males that survived were children\
 they too were taken first. First preferences to the survival of passengers was given to females and children.'

data = [passengers]
data1 = [male_passengers,female_passengers]
data2 = [p_survived,p_died]
data3 = [f_survived,f_deaths,m_survived,m_deaths]
data4 = [f_survived,m_survived]
data5 = [f_deaths,m_deaths]


plt.xlabel('Number of Titanic Passengers')
plt.ylabel('Total')
plt.title('Titanic Passengers')
plt.hist(data) #get the data for display
plt.show()

plt.xlabel('Number of Male VS Female Passengers')
plt.ylabel('Total')
plt.title('Male and Female Passengers')
plt.hist(data1)
plt.show()

plt.xlabel('Number of Survivals VS Number of Deaths')
plt.ylabel('Total')
plt.title('Passenger Survival and Deaths')
plt.hist(data2)
plt.show()

plt.xlabel('Number of Male VS Female Survival and Deaths')
plt.ylabel('Total')
plt.title('Male and Female Survival and Deaths')
plt.hist(data3)
plt.show() #display the graph

plt.xlabel('Number of Deaths VS Number of Survivals')
plt.ylabel('Total')
plt.title('Male and Female That Survived and Died')
plt.plot(data4, label = 'Survived Male and Female')
#plt.show()
plt.plot(data5, label = 'Male and Female That Died')
plt.legend()
plt.show()
