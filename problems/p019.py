from datetime import datetime, date
from dateutil.relativedelta import relativedelta

if __name__ == '__main__':

    start_date = "1901-01-01"

    dtObj = datetime.strptime(start_date, "%Y-%m-%d")

    n = 1

    count_sundays = 0

    while (dtObj.year < 2001):

        current_date = dtObj.date()

        current_date_weekday = current_date.strftime("%w")

        #print(current_date)
        
        #print(current_date_weekday)
        
        if (current_date_weekday == '0'):
            count_sundays += 1

        future_date = str((dtObj + relativedelta(months=n)).date())

        dtObj = datetime.strptime(future_date, "%Y-%m-%d")

    print("Total sundays: " + str(count_sundays))
