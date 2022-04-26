import datetime


def time_input():
    time = input()
    time_value = datetime.datetime.strptime(time, "%H %M")
    return time_value


def add_time(l_time, t_time):
    dest_time = datetime.timedelta(hours=l_time.hour, minutes=l_time.minute) + datetime.timedelta(hours=t_time.hour, minutes=t_time.minute)
    # print(dest_time)
    d_time = (str(dest_time)).split(":")
    # print(d_time)
    try:
        s_time = int(d_time[0])
    except ValueError:
        s_time = d_time[0].split(",")
        s_value = int(s_time[1])
        d_time[0] = str(s_value).zfill(2)
    else:
        d_time[0] = str(s_time).zfill(2)
    finally:
        return f"{d_time[0]} {d_time[1]}"


launch_time = time_input()
travel_time = time_input()
print(add_time(launch_time, travel_time))
