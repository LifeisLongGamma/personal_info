name = input('What is your name: ')
surname = input('What is your surname: ')
hometown = input('What is your hometown: ')
birth_year = int(input('What is the year of your birth: '))
school = int(input('What is the number of your school: '))
university = input('What university did you graduate from: ')
profession = input('What is your current profession: ')

madlib = f'My name is {name} {surname}. I was born in {hometown} in {birth_year}. \
I completed the school {school} and graduated from {university}. Currently I work as a {profession}.'

print(madlib)
