#! /usr/bin/env python
# -*- encoding: UTF-8 -*-

"""$ fun.py --ip $YOUR_ROBOTS_IP_ADDRESS"""

import qi
import argparse
import sys
import time
from naoqi import ALProxy


def main(robotIP, PORT=9559):
    """
    This is the basic schedule dialog.
    """
    tts = ALProxy("ALAnimatedSpeech", robotIP, PORT)
    # enable gestures
    # tts = session.service("ALAnimatedSpeech")

    # The robot shares the daily schedule
    tts.say("^start(animations/Stand/Gestures/Hey_1) Good morning! I am your friend the NAO robot. ^stop(animations/Stand/Gestures/Hey_1) Here is your schedule for the day.")
    tts.say("^start(animations/Stand/Gestures/Enthusiastic_4) First you will have breakfast. The menu is eggs, bacon, pancakes, and orange juice. I wish I could eat that! ^stop(animations/Stand/Gestures/Enthusiastic_4)")
    tts.say("^start(animations/Stand/Gestures/You_1) Next it is time to take your medication. ^stop(animations/Stand/Gestures/You_1) ")
    tts.say("^start(animations/Stand/Gestures/Enthusiastic_5) After that Nurse Jenny will check in on you. She is nice! ^stop(animations/Stand/Gestures/Enthusiastic_5)")
    tts.say("^start(animations/Stand/Gestures/Explain_8) Next is play time and you can choose to go to the game room, or the library. I think you're cool, and that's nonfiction! ^start(animations/Stand/Gestures/Explain_8)")
    tts.say("After that is Lunch. The menu is Mac n cheese, apple sauce, and milk. Tasty!")
    tts.say("^start(animations/Stand/Gestures/Enthusiastic_5) Next it will be time to do your schoolwork. I always angled for straight Ayess on my geometry exams! ^start(animations/Stand/Gestures/Enthusiastic_5)")
    tts.say("^start(animations/Stand/Gestures/You_4) After that you will get a visit from your brother. Yipee! ^stop(animations/Stand/Gestures/You_4)")
    tts.say("^start(animations/Stand/Gestures/Explain_10) Next it is time to get a CT scan of your lungs. ^stop(animations/Stand/Gestures/Explain_10)")
    tts.say("^start(animations/Stand/Gestures/Enthusiastic_4) After that Dr. Jones will come check up on you. She is the best! ^stop(animations/Stand/Gestures/Enthusiastic_4)")
    tts.say("Next it is dinner time. The menu is dinosaur chicken nuggets, sweet potato fries, ketchup, broccoli and kool aid. What day do chickens fear the most? Fry-days!")
    tts.say("^start(animations/Stand/Gestures/You_1) After that it is time to take your medication ^stop(animations/Stand/Gestures/You_1)")
    tts.say("Next Nurse Blain will check in on you. He is my favorite!")
    tts.say("^start(animations/Stand/Gestures/Hey_6) Finally after that it is bedtime. Goodnight! Dont let the bed bugs bite! If they do, hit them with a shoe, until they're black and blue! ^stop(animations/Stand/Gestures/Hey_6)")

    tts.setParameter("pitchShift", 0)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", type=str, default="127.0.0.1",
                        help="Robot IP address. On robot or Local Naoqi: use '127.0.0.1'.")
    parser.add_argument("--port", type=int, default=9559,
                        help="Naoqi port number")

    args = parser.parse_args()
    main(args.ip, args.port)