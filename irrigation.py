# import Rpi.GPIO as GPIO
import time
import os
# import RPi.GPIO as GPIO
import time
import pandas as pd



# variables
schedule_file = "schedule.txt"
update = 1
# ouverture du fichier de schedules
zones = []
hours = []
durations = []
on = []
off = []

#
# #set GPIO mode
# GPIO.setmode(GPIO.BOARD)
# gpio_ports=[11,12,13,15,16,18,22]
#
# print(time.time())
# for i in mylist:
#     GPIO.setup(i, GPIO.OUT)
#     GPIO.output(i, False)
#
# time.sleep(2)
# for j in mylist:
#     GPIO.output(j, True)
#
# GPIO.cleanup()



def GPIO_port():
    with open("zones.txt", "r") as f:
        for row in f.read().split("\n"):
            if "," in row:
                zone, hour, duration = row.split(",")
                zones.append(str(zone))
                hours.append(str(hour))
                durations.append(int(duration))
                on.append(int(hour.split(":")[0])*60 + int(hour.split(":")[1]))
                off.append(int(on[-1]) + int(duration))


# unpack schedules
def unpack(schedfile):
    global zones, hours, durations, on, off

    # with open(schedfile, "r") as f:
    #     for row in f.read().split("\n"):
    #         if "," in row:
    #             zone, hour, duration = row.split(",")
    #             zones.append(str(zone))
    #             hours.append(str(hour))
    #             durations.append(int(duration))
    #             on.append(int(hour.split(":")[0])*60 + int(hour.split(":")[1]))
    #             off.append(int(on[-1]) + int(duration))

    schedule = pd.read_csv(schedfile)
    return schedule


def Main():
    # while True:
    schedule = pd.read_csv("schedule.txt").set_index('zone')
    zones = pd.read_csv("zones.txt").set_index('zone')

    schedule = schedule.join(zones)
    schedule['on'] = schedule.start.apply(lambda x:int(x.split(":")[0]))*60 + schedule.start.apply(lambda x:int(x.split(":")[1]))
    schedule['off'] = schedule.on + schedule.duration

    print(schedule)


    now = (int(time.strftime("%H",  time.localtime(time.time())).split(":")[0])*60) + int(time.strftime("%M",  time.localtime(time.time())).split(":")[0])

    schedule.reset_index(inplace = True)
    for z in schedule.index:
        if now >= schedule.at[z,'on'] and now < schedule.at[z,'off'] :
            print(schedule.at[z,'zone'], "ON")
        else:
            print(schedule.at[z,'zone'], "OFF")

    print(now, str(int(now/60)) + "h" + str(now % 60))





Main()
