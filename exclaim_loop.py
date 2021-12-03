#! /usr/bin/env python
# -*- encoding: UTF-8 -*-

"""$ exclaim.py --ip $YOUR_ROBOTS_IP_ADDRESS"""

import qi
import argparse
import sys
import time
from naoqi import ALProxy
import csv

def main(robotIP, PORT=9559):
    """
    This is the basic schedule dialog.
    """
    
    with open('schedule.csv', newline='') as f:
        reader = csv.reader(f)
        schedule = list(reader)

    alternate = True
    
    animated = ALProxy("ALAnimatedSpeech", robotIP, PORT)
    configuration = {"bodyLanguageMode":"disabled"} 

    animation_list = [["^start(animations/Stand/Gestures/Explain_2)", "^stop(animations/Stand/Gestures/Explain_2)"], ["^start(animations/Stand/Gestures/Explain_3)", "^stop(animations/Stand/Gestures/Explain_3)"]]
    
    config = 1
    # The robot shares the daily schedule
    animated.say(" Good morning! I am the NAO robot. Here is your schedule for the day. ", configuration)
    for item in schedule:
        if config mod 3 == 0:
            animated.say(item, configuration)
        elif alternate:
            animated.say(animation_list[0[0]] + item + animation_list[0[1]])
        else:
            animated.say(animation_list[1[0]] + item + animation_list[1[1]])
        alternate = not alternate
        config = config + 1

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", type=str, default="127.0.0.1",
                        help="Robot IP address. On robot or Local Naoqi: use '127.0.0.1'.")
    parser.add_argument("--port", type=int, default=9559,
                        help="Naoqi port number")

    args = parser.parse_args()
    main(args.ip, args.port)