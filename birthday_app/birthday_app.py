import datetime


def print_header():
    print('--------------------')
    print('   BIRTHDAY APP     ')
    print('--------------------')


def get_birthday_from_user():
    print('When were you born?')
    year = input('Year [YYYY]:')
    month = input('Month [MM]:')
    day = input('Day [DD]:')

    birthday = datetime.date(int(year), int(month), int(day))
    return birthday


def compute_days_between_dates(original_date, target_date):
    this_year = datetime.date(target_date.year, original_date.month, original_date.day)
    dt = this_year - target_date
    return dt.days


def print_birthday_information(days):
    if days < 0:
        print('You had birthday {} days ago this year.'.format(-days))
    elif days > 0:
        print('your birthday is in {} days!'.format(days))
    else:
        print('Happy birthday!')


def main():
    print_header()
    birthday = get_birthday_from_user()
    print(birthday)
    today = datetime.date.today()
    number_of_days = compute_days_between_dates(birthday, today)
    print_birthday_information(number_of_days)


main()
