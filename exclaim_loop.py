#! /usr/bin/env python
# -*- encoding: UTF-8 -*-

"""$ exclaim.py --ip $YOUR_ROBOTS_IP_ADDRESS"""

import qi
import argparse
import sys
import time
from naoqi import ALProxy
import csv

class Appointment:
    def __init__(self, name, hr, minute):
        self.name = name
        self.hour = hr
        self.minute = minute

    def getMinutesTilEvent(self):
        t = time.localtime(time.time())
        time_in_min = t.tm_hour * 60 + t.tm_min
        app_in_min = int(self.hour) * 60 + int(self.minute)
        return app_in_min - time_in_min
        
    def getStatement(self):
        return ("At " + str(self.hour) + " " + str(self.minute) + " you have " + str(self.name))


def read_csv():
    with open('schedule.csv') as f:
        reader = csv.reader(f)
        schedule = list(reader)
        print(schedule)
        schedule = schedule[0]
        appointmentlist = []
        for i in range(len(schedule)/3):
            name = schedule[3*i]
            hour = schedule[3*i+1]
            minute = schedule[3*i+2]
            app = Appointment(name, hour, minute)
            appointmentlist.append(app)
        return appointmentlist



def main(robotIP, PORT=9559):
    """
    This is the basic schedule dialog.
    """
    previous_schedule = []
    current_schedule = read_csv()
    previous_time = time.localtime(time.time())
    current_time = time.localtime(time.time())
    first_reading = True

    while(True):
        
        alternate = True
    
        animated = ALProxy("ALAnimatedSpeech", robotIP, PORT)
        configuration = {"bodyLanguageMode":"disabled"} 

        animation_list = [["^start(animations/Stand/Gestures/Explain_2)", "^stop(animations/Stand/Gestures/Explain_2)"], ["^start(animations/Stand/Gestures/Explain_3)", "^stop(animations/Stand/Gestures/Explain_3)"]]
    
        config = 1

        if len(current_schedule) == len(previous_schedule):
            for i in range(len(current_schedule)):
                current_appointment = current_schedule[i]
                previous_appointment = previous_schedule[i]
                if(current_appointment.name != previous_appointment.name or current_appointment.minute != previous_appointment.minute or current_appointment.hour != previous_appointment.hour):
                    animated.say(" Hello. An item in your schedule has been changed. Instead of ", configuration)
                    animated.say(previous_appointment.name + " at " + previous_appointment.hour + " " + previous_appointment.minute, configuration)
                    animated.say(" you have " + current_appointment.name + " at " + current_appointment.hour + " " + current_appointment.minute, configuration)
                    previous_schedule = current_schedule
        else:
            #The robot shares the daily schedule
            if first_reading:
                animated.say("Good Morning. I am the NAO robot. Here is your schedule for today.", configuration)
                previous_schedule = current_schedule
                first_reading=False
            else:
                animated.say("Your schedule has changed", configuration)
                previous_schedule = current_schedule
                
            for item in current_schedule:
                s = item.getStatement()
                print(s)
                animated.say(s)
        
        #Then, compare the current time to the soonest event in the schedule
        previous_time = current_time
        current_time = time.localtime(time.time())

        if current_time.tm_min != previous_time.tm_min:
            #Get the new schedule
            previous_schedule = current_schedule
            current_schedule = read_csv()
            for app in current_schedule:
                if app.getMinutesTilEvent() == 0:
                    # If it is time for an event, then announce the event
                    animated.say("Since it is " + app.hour + " " + app.minute + " it is time for " + app.name + ". Let's go!", configuration)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", type=str, default="127.0.0.1",
                        help="Robot IP address. On robot or Local Naoqi: use '127.0.0.1'.")
    parser.add_argument("--port", type=int, default=9559,
                        help="Naoqi port number")

    args = parser.parse_args()
    main(args.ip, args.port)
