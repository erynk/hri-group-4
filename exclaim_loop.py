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
    def __init__(self, name, hr, min):
        self.name = name
        self.hour = hour
        self.minute = min


def read_csv()
    with open('schedule.csv', newline='') as f:
        reader = csv.reader(f)
        schedule = list(reader)
        appointmentlist = []
        for i in range(len(schedule)):
            name = schedule[i]
            i = i + 1
            hour = schedule[i]
            i = i + 1
            minute = schedule[i]
            app = Appointment(name, hour, minute)
            appointmentlist.append(app)
        return appointmentlist



def main(robotIP, PORT=9559):
    """
    This is the basic schedule dialog.
    """
    previous_schedule = []
    current_schedule = []

    while(True):
        #Get the new schedule
        previous_schedule = current_schedule
        current_schedule = read_csv()
        
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
                    animated.say(" Hello. Your schedule has changed. Instead of", configuration)
                    animated.say(previous_appointment.name + "at" + previous_appointment.hour + " " + previous_appointment.minute, configuration)
                    animated.say("you have" + current_appointment.name + "at" + current_appointment.hour + " " + current_appointment.minute, configuration)
        else
             The robot shares the daily schedule
            animated.say("I am the NAO robot. New items have been uploaded to the schedule", configuration)
            for item in schedule:
                if config mod 3 == 0:
                    animated.say(item, configuration)
                elif alternate:
                    animated.say(animation_list[0[0]] + item + animation_list[0[1]])
                else:
                    animated.say(animation_list[1[0]] + item + animation_list[1[1]])
                alternate = not alternate
                config = config + 1
        
        #Then, compare the current time to the soonest event in the schedule
        current_time = time.localtime(time.time())

        #If it is time for an event, then announce the event 

    #

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", type=str, default="127.0.0.1",
                        help="Robot IP address. On robot or Local Naoqi: use '127.0.0.1'.")
    parser.add_argument("--port", type=int, default=9559,
                        help="Naoqi port number")

    args = parser.parse_args()
    main(args.ip, args.port)