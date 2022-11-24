import datetime


def dict_convert_datetime_hhmm(dic):
    """Takes dictionary and converts its values from datetime to format hhmm """

    # Loops through each key and breaks down the datetime.timedelta objects to hours and minutes strings
    for key in dic.keys():
        seconds = dic[key].seconds
        days_to_hours = dic[key].days * 24
        hours = seconds // 3600
        minutes = (seconds // 60) - (hours * 60)
        dic[key] = str(hours + days_to_hours) + ":" + str(minutes)

    return dic
