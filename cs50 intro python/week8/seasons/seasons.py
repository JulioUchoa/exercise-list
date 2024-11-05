# import needed libs
import sys
import inflect
from datetime import date, datetime


# define Date() Class. it will convert users input from YYYY-MM-DD to total minutes from their birthday
class Date():
    def __init__(self, birthday):
        self.birthday = birthday

    def conv(self):
        try:
            year, month, day = self.birthday.split("-")
            year = int(year)
            month = int(month)
            day = int(day)
            birth = datetime(year, month, day)

            today = date.today()
            y = today.year
            m = today.month
            d = today.day
            today = datetime(y, m, d)

            final = today - birth
            total_min = final.days * 24 * 60

            p = inflect.engine()

            word = p.number_to_words(total_min).replace(" and", "").capitalize()
            return word + " minutes"


        except:
            sys.exit("Invalid Input")

def main():
# get users input
    birthday = input("Date of Birth: ")
    d = Date(birthday)
    return print(d.conv())



if __name__ == '__main__':
    main()
