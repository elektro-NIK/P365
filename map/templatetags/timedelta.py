from django import template
register = template.Library()


@register.filter()
def timedelta(timedelta_obj):
    secs = timedelta_obj.total_seconds()
    res = ""
    flag = False
    if secs > 24 * 60 * 60:
        flag = True
        days = secs // (24 * 60 * 60)
        res += "{} d ".format(int(days))
        secs = secs - days * 24 * 60 * 60
    if secs > 60 * 60:
        hrs = secs // (60 * 60)
        res += "{}:".format(int(hrs))
        secs = secs - hrs * 60 * 60
    elif flag:
        hrs = 0
        res += "{}:".format(int(hrs))
    if secs > 60:
        mins = secs // 60
        res += "{}:".format(int(mins))
        secs = secs - mins * 60
    elif flag:
        mins = 0
        res += "{}:".format(int(mins))
    if secs >= 0:
        res += "{}".format(int(secs))
    return res
