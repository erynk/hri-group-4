#! /usr/bin/env python
# -*- encoding: UTF-8 -*-

"""$ boring.py --ip $YOUR_ROBOTS_IP_ADDRESS"""

import qi
import argparse
import sys
import time


def main(session):
    """
    This is the basic schedule dialog.
    """
    tts = session.service("ALTextToSpeech")
    
    # set boring params
    tts.setParameter("pitchShift", 0)
    tts.setParameter("pitchShift", 0.65)

    # The robot shares the daily schedule
    tts.say("I am the NAO robot. Here is your schedule for the day.")
    tts.say("First you will have breakfast. The menu is eggs, bacon, pancakes, and orange juice.")
    tts.say("Next it is time to take your medication.")
    tts.say("After that Nurse Jenny will check in on you.")
    tts.say("Next is play time and you can choose to go to the game room, or the library.")
    tts.say("After that is Lunch. The menu is Mac n cheese, apple sauce, and milk.")
    tts.say("Next it will be time to do your school work.")
    tts.say("After that you will get a visit from your brother.")
    tts.say("Next it is time to get a CT scan of your lungs.")
    tts.say("After that Dr. Jones will come check up on you.")
    tts.say("Next it is dinner time. The menu is chicken nuggets, sweet potato fries, ketchup, broccoli, and kool aid.")
    tts.say("After that it is time to take your medication")
    tts.say("Next Nurse Blain will check in on you.")
    tts.say("Finally after that it is bedtime.")

    tts.setParameter("pitchShift", 0)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", type=str, default="127.0.0.1",
                        help="Robot IP address. On robot or Local Naoqi: use '127.0.0.1'.")
    parser.add_argument("--port", type=int, default=9559,
                        help="Naoqi port number")

    args = parser.parse_args()
    session = qi.Session()
    try:
        session.connect("tcp://" + args.ip + ":" + str(args.port))
    except RuntimeError:
        print ("Can't connect to Naoqi at ip \"" + args.ip + "\" on port " + str(args.port) +".\n"
               "Please check your script arguments. Run with -h option for help.")
        sys.exit(1)
    main(session)