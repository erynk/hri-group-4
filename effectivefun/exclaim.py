#! /usr/bin/env python
# -*- encoding: UTF-8 -*-

"""$ exclaim.py --ip $YOUR_ROBOTS_IP_ADDRESS"""

import qi
import argparse
import sys
import time
from naoqi import ALProxy

def main(robotIP, PORT=9559):
    """
    This is the basic schedule dialog.
    """
    animated = ALProxy("ALAnimatedSpeech", robotIP, PORT)
    tts = ALProxy("ALTextToSpeech", robotIP, PO)

    # The robot shares the daily schedule
    tts.say(" Good morning! I am the NAO robot. Here is your schedule for the day. ")
    animated.say("^start(animations/Stand/Gestures/Explain_2) First you will have breakfast. The menu is eggs, bacon, pancakes, and orange juice. Yay! Pancakes! ^stop(animations/Stand/Gestures/Explain_2)")
    tts.say(" Next it is time to take your medication.")
    animated.say("^start(animations/Stand/Gestures/Explain_3) After that Nurse Jenny will check in on you. She is nice! ^stop(animations/Stand/Gestures/Explain_3)")
    tts.say("  Next is play time and you can choose to go to the game room, or the library. Fun! ")
    animated.say("^start(animations/Stand/Gestures/Explain_2) After that is Lunch. The menu is Mac n cheese, apple sauce, and milk. Tasty! ^stop(animations/Stand/Gestures/Explain_2)")
    tts.say(" Next it will be time to do your school work. ")
    tts.say(" After that you will get a visit from your brother. Yipee! ")
    tts.say(" Next it is time to get a CT scan of your lungs. ")
    animated.say("^start(animations/Stand/Gestures/Explain_3) After that Dr. Jones will come check up on you. She is the best! ^stop(animations/Stand/Gestures/Explain_3)")
    animated.say("^start(animations/Stand/Gestures/Explain_2) Next it is dinner time. The menu is chicken nuggets, sweet potato fries, ketchup, broccoliand kool aid. Yum! ^stop(animations/Stand/Gestures/Explain_2)")
    tts.say(" After that it is time to take your medication ")
    animated.say("^start(animations/Stand/Gestures/Explain_2) Next Nurse Blain will check in on you. He is my favorite! ^stop(animations/Stand/Gestures/Explain_2)")
    animated.say("^start(animations/Stand/Gestures/Explain_3) Finally after that it is bedtime. Goodnight! ^stop(animations/Stand/Gestures/Explain_3)")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", type=str, default="127.0.0.1",
                        help="Robot IP address. On robot or Local Naoqi: use '127.0.0.1'.")
    parser.add_argument("--port", type=int, default=9559,
                        help="Naoqi port number")

    args = parser.parse_args()
    main(args.ip, args.port)