import datetime

today = datetime.date.today()

year = today.year

birth_year = input ("Enter your birth year: ")

age = year - int(birth_year)
print ("You are or turning " + str(age))