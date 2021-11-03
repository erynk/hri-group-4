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
    tts.say("^start(animations/Stand/Gestures/Enthusiastic_4) Enthusiastic 4. The quick brown fox jumps over the lazy dog. ^wait(animations/Stand/Gestures/Enthusiastic_4)")
    tts.say("^start(animations/Stand/Gestures/Enthusiastic_5) Enthusiastic 5. The quick brown fox jumps over the lazy dog. ^wait(animations/Stand/Gestures/Enthusiastic_5)")
    tts.say("^start(animations/Stand/Gestures/Explain_1) Explain 1. The quick brown fox jumps over the lazy dog. ^wait(animations/Stand/Gestures/Explain_1)")
    tts.say("^start(animations/Stand/Gestures/Explain_2) Explain 2. The quick brown fox jumps over the lazy dog. ^wait(animations/Stand/Gestures/Explain_2)")
    tts.say("^start(animations/Stand/Gestures/Explain_3) Explain 3. The quick brown fox jumps over the lazy dog. ^wait(animations/Stand/Gestures/Explain_3)")
    tts.say("^start(animations/Stand/Gestures/Please_1) Please 1. The quick brown fox jumps over the lazy dog. ^wait(animations/Stand/Gestures/Please_1)")
    tts.say("^start(animations/Stand/Gestures/You_1) You 1. The quick brown fox jumps over the lazy dog. ^wait(animations/Stand/Gestures/You_1)")
    tts.say("^start(animations/Stand/Gestures/BodyTalk_1) Body Talk 1. The quick brown fox jumps over the lazy dog. ^wait(animations/Stand/Gestures/BodyTalk_1)")

    tts.setParameter("pitchShift", 0)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", type=str, default="127.0.0.1",
                        help="Robot IP address. On robot or Local Naoqi: use '127.0.0.1'.")
    parser.add_argument("--port", type=int, default=9559,
                        help="Naoqi port number")

    args = parser.parse_args()
    main(args.ip, args.port)