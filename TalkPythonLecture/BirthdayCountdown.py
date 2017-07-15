import datetime

def header():
    print('---------------------------------------')
    print('           Birthday App')
    print('---------------------------------------')

def get_bday_from_user():
    year = int(input('What year?:'))
    month = int(input('What month?:'))
    day = int(input('What day?:'))
    birthday = datetime.datetime(year,month,day)
    return birthday

def compute_days_between(bday, now):
    now1 = datetime.datetime(now.year, bday.month, bday.day)
    dt = now1-now
    days = int(dt.total_seconds()/60/60/24)
    return days

def print_bday_info(ddays):
    if ddays < 0:
        print('Your birthday was {} days ago'.format(ddays))
    elif ddays > 0:
        print('Your birthdays is in {} days'.format(ddays))
    else:
        print('Happy Birthday!!!')

def main():
    header()
    bday = get_bday_from_user()
    now = datetime.datetime.now()
    ddays = compute_days_between(bday, now)
    print_bday_info(ddays)

main()