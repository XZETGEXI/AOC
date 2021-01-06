from utilities import *

log = logger()

log("Logger in")

TEXTUP = "wakes up"
TEXTSLEEP = "falls asleep"

def get_d():
    d_date_guard = {}
    d_guard_date = defaultdict(list)
    d_date_sleeps = defaultdict(lambda: defaultdict(list))

    data = read("input.txt")
    for i in data:
        timestamp, msg = i
        ymd, t = format_date(timestamp)
        if "#" in msg:
            guard_id = get_id(msg)
            d_date_guard[ymd] = guard_id, t
            d_guard_date[guard_id].append((ymd, t))
        else:
            d_date_sleeps[ymd][msg].append(t)
    
    d_guard_date = round_next_day(d_guard_date)
    
    d_argname_arg = packer([d_date_guard, d_guard_date, d_date_sleeps])
    return d_argname_arg

def calculate_time_asleep(d_date_sleeps, date):
    pos = sum([i.minute for i in d_date_sleeps[date][TEXTUP]])
    neg = sum([i.minute for i in d_date_sleeps[date][TEXTSLEEP]])
    return pos - neg

def calculate_total_time_asleep(d_argname_arg):
    d_guard_sleep = {}
    
    d_guard_date = d_argname_arg["arg1"]
    d_date_sleeps = d_argname_arg["arg2"]
    for guard in d_guard_date:
        time_asleep = 0
        for date in d_guard_date[guard]:
            time_asleep += calculate_time_asleep(d_date_sleeps, date[0])
        d_guard_sleep[guard] = time_asleep
    
    return d_guard_sleep

def calculate_minute(d_argname_arg, guard, part = "silver"):
    sleeps = []
    
    d_guard_date = d_argname_arg["arg1"]
    d_date_sleeps = d_argname_arg["arg2"]
    for date in d_guard_date[guard]:
        ymr = date[0]
        sleeps.append(d_date_sleeps[ymr])
    
    d_score_minute, d_minute_score = get_score_minute(sleeps)
    if part == "silver":
        return int(d_score_minute[max(d_score_minute)])
    elif part == "gold":
        d_max_minute = {max(d_score_minute): d_score_minute[max(d_score_minute)]}
        return d_max_minute

def get_score_minute(sleeps):
    d_minute_score = defaultdict(int)
    
    for day in sleeps:
        asleep = 0
        for check_minute in range(60):
            timestamp = datetime.time(hour = 0, minute = check_minute)
            if timestamp in day[TEXTSLEEP]:
                asleep = 1
            elif timestamp in day[TEXTUP]:
                asleep = 0
            d_minute_score[check_minute] += asleep
    
    d_score_minute = revert_d(d_minute_score)
    return d_score_minute, d_minute_score

def silver():
    d_argname_arg = get_d()
    d_guard_sleep = calculate_total_time_asleep(d_argname_arg)
    d_sleep_guard = revert_d(d_guard_sleep)
    most_asleep_time = max(d_sleep_guard)
    most_asleep_guard = d_sleep_guard[most_asleep_time]
    minute_most_asleep = calculate_minute(d_argname_arg, most_asleep_guard, part = "silver")
    return minute_most_asleep * int(most_asleep_guard)

def gold():
    d_argname_arg = get_d()
    d_guard_date = d_argname_arg["arg1"]
    d_maxsleep_guard = {}
    d_maxsleep_minute = {}
    
    for guard in d_guard_date:
        d_max_minute = calculate_minute(d_argname_arg, guard, part = "gold")
        max_sleep = [*d_max_minute.keys()][0]
        d_maxsleep_guard[max_sleep] = guard
        d_maxsleep_minute[max_sleep] =  d_max_minute[max_sleep]
    max_sleep = max(d_maxsleep_guard)
    
    return d_maxsleep_minute[max_sleep] * int(d_maxsleep_guard[max_sleep])
        
if __name__ == "__main__":
    start = tic()
    start = toc(start)
    log("Silver", silver())
    step = toc(start)
    log("Gold", gold())
    end = toc(step)
