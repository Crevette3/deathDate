#!python3
#https://www.youtube.com/channel/UCsZs-p37pse_4UXG-alR47w   (My channel where I explain this code and demonstrate it working)
#deathDate.py - Estimates the year you will die based on the data from csv file
import pandas as pd
import datetime
from datetime import timedelta

monthsOfYear = ('0', 'January', 'Febuary', 'March', 'April',
                'May', 'June', 'July', 'August', 'September',
                'October', 'November', 'December')
print('Make sure to use correct spelling and capitalization.')
while True:
    try:
        
        userInputBirthCountry = input('What country were you born in?: ')
        userInputBirthDay = input('Enter Birthday in YYYY-MM-DD format: ')

        birthYear, birthMonth, birthDay = map(int, userInputBirthDay.split('-'))
        formatedBirthDate = datetime.date(birthYear, birthMonth, birthDay)
                        
        reader = pd.read_csv('LifeExpectancy.csv', header = 2)

        returnedLifeSpan = (reader[reader["Country Name"] == userInputBirthCountry][str(birthYear)])

        lifeSpan = int(round(returnedLifeSpan))
        break
    except:
        print('\n!!!Check that spelling and capitalization are correct\n'+
              'and that your birthday is in the correct format!!!\n')


totalDays = lifeSpan * 365
deathYear = formatedBirthDate + timedelta(days=totalDays)


print('\nThe average lifespan of a person born on ' + monthsOfYear[formatedBirthDate.month] + ' ' +
        str(formatedBirthDate.day) + ', ' + str(formatedBirthDate.year) + ' is ' + str(lifeSpan) + ' years.')

print('You could also say that your average lifespan is ' + str(totalDays) + ' days.')

print('So if all goes well you should live to see year ' + str(deathYear.year))
