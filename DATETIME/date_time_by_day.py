from datetime import datetime, timedelta

weekdays = [
    'Monday',
    'Tuesday',
    'Wednesday',
    'Thursday',
    'Friday',
    'Saturday',
    'Sunday'
]


def get_date_time_by_day(day_name, start_date=None):
    """
    Get DateTime by day name
    :param day_name:
    :param start_date:
    :return:
    """
    if start_date is None:
        start_date = datetime.today()
    day_num = start_date.weekday()
    day_num_target = weekdays.index(day_name)
    days_ago = (7 + day_num - day_num_target) % 7
    if days_ago == 0:
        days_ago = 7
    target_date = start_date - timedelta(days=days_ago)
    return target_date


print(get_date_time_by_day('Tuesday'))
# The optional start_date can be supplied using another datetime instance.
print(get_date_time_by_day('Sunday', datetime(2020, 11, 10)))
