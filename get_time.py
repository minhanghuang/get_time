import datetime
import calendar
now = datetime.datetime.now()


def get_time(year=now.year,
             month=now.month,
             day=now.day,
             hour=now.hour,
             minute=now.minute,
             second=now.second,
             week=-1,
             last_day_of_month=False,
             type="time",
             detail=True):
    """
    获取 00:00:00
    :param year: 年 (默认今年)
    :param month: 月 (默认当月)
    :param day: 天 (默认今天)
    :param hour: 时 (默认今天)
    :param minute: 分 (默认今天)
    :param second: 秒 (默认今天)
    :param week: 星期x (默认-1,如果不等于-1,则day参数无效)
    :param last_day_of_month: 每个月的最后一天 (默认False)
    :param type: 输出类型 (默认今天)
    :param detail: 是否输出时分秒? (默认输出时分秒)
    :return: time (type datetime / str)
    """

    if week != -1:
        weekday = now - \
                  datetime.timedelta(hours=hour,
                            minutes=minute,
                            seconds=second,
                            microseconds=now.microsecond)

        one_day = datetime.timedelta(days=1)
        while weekday.weekday() != 0:
            weekday -= one_day

        ret = weekday + datetime.timedelta(days=week-1)

    else:

        if last_day_of_month: # 每个月的最后一天
            day = calendar.monthrange(year, month)[1]

        if not detail:
            date = datetime.date(year, month, day)
        else:
            date = datetime.datetime(year, month, day, hour, minute, second)

        ret = date if type == "time" else str(date)

    return ret

