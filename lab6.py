#! /usr/bin/env python
# -*- encoding: UTF-8 -*-

"""Example: PoseInit - Small example to make Nao go to an initial position."""

import qi
import argparse
import sys
# Choregraphe simplified export in Python.
from naoqi import ALProxy
names = list()
times = list()
keys = list()


def main(session):
    """
    PoseInit: Small example to make Nao go to an initial position.
    """
    # Get the services ALMotion & ALRobotPosture.

    motion_service = session.service("ALMotion")
    posture_service = session.service("ALRobotPosture")

    # Wake up robot
    motion_service.wakeUp()

    # Send robot to Stand Init
    posture_service.goToPosture("StandInit", 0.5)

    names.append("HeadPitch")
    times.append([0.96, 1.76, 2.56, 3.56, 4.72, 5.52, 7.16, 8.8])
    keys.append([0.514872, 0.514872, 0.514872, 0.514872, 0.514872, 0.514872, 0.514872, 0.514872])

    names.append("HeadYaw")
    times.append([0.96, 1.76, 2.56, 3.56, 4.72, 5.52, 7.16, 8.8])
    keys.append([-0.024586, -0.024586, -0.024586, -0.024586, -0.024586, -0.024586, -0.024586, -0.024586])

    names.append("LAnklePitch")
    times.append([0.96, 1.76, 2.56, 3.56, 4.72, 5.52, 7.16, 8.8])
    keys.append([-0.291502, -0.346726, -0.37127, -0.405018, -0.415756, -0.426494, -0.437232, -0.47098])

    names.append("LAnkleRoll")
    times.append([0.96, 1.76, 2.56, 3.56, 4.72, 5.52, 7.16, 8.8])
    keys.append([0.0353239, 0.0353239, 0.0353239, 0.04913, 0.04913, 0.04913, 0.0598679, 0.0598679])

    names.append("LElbowRoll")
    times.append([0.96, 1.76, 2.56, 3.56, 4.72, 5.52, 7.16, 8.8])
    keys.append([-0.0383081, -0.0383081, -0.0383081, -0.0383081, -0.0383081, -0.0383081, -0.0383081, -0.0383081])

    names.append("LElbowYaw")
    times.append([0.96, 1.76, 2.56, 3.56, 4.72, 5.52, 7.16, 8.8])
    keys.append([-0.825334, -0.825334, -0.825334, -0.825334, -0.825334, -0.825334, -0.825334, -0.825334])

    names.append("LHand")
    times.append([0.96, 1.76, 2.56, 3.56, 4.72, 5.52, 7.16, 8.8])
    keys.append([0.0252, 0.0252, 0.0252, 0.0252, 0.0252, 0.0252, 0.0252, 0.0252])

    names.append("LHipPitch")
    times.append([0.96, 1.76, 2.56, 3.56, 4.72, 5.52, 7.16, 8.8])
    keys.append([0.48398, 0.48398, 0.48398, 0.48398, 0.48398, 0.48398, 0.48398, 0.48398])

    names.append("LHipRoll")
    times.append([0.96, 1.76, 2.56, 3.56, 4.72, 5.52, 7.16, 8.8])
    keys.append([-0.133416, -0.133416, -0.133416, -0.133416, -0.133416, -0.133416, -0.133416, -0.133416])

    names.append("LHipYawPitch")
    times.append([0.96, 1.76, 2.56, 3.56, 4.72, 5.52, 7.16, 8.8])
    keys.append([-0.420274, -0.4034, -0.392662, -0.377322, -0.377322, -0.377322, -0.377322, -0.377322])

    names.append("LKneePitch")
    times.append([0.96, 1.76, 2.56, 3.56, 4.72, 5.52, 7.16, 8.8])
    keys.append([0.184038, 0.31136, 0.346642, 0.400332, 0.41107, 0.41107, 0.421808, 0.45709])

    names.append("LShoulderPitch")
    times.append([0.96, 1.76, 2.56, 3.56, 4.72, 5.52, 7.16, 8.8])
    keys.append([1.37442, 1.37442, 1.37442, 1.37442, 1.37442, 1.37442, 1.37442, 1.37442])

    names.append("LShoulderRoll")
    times.append([0.96, 1.76, 2.56, 3.56, 4.72, 5.52, 7.16, 8.8])
    keys.append([-0.0583339, -0.0583339, -0.0583339, -0.0583339, -0.0583339, -0.047596, -0.047596, -0.047596])

    names.append("LWristYaw")
    times.append([0.96, 1.76, 2.56, 3.56, 4.72, 5.52, 7.16, 8.8])
    keys.append([0.121144, 0.121144, 0.121144, 0.121144, 0.121144, 0.121144, 0.121144, 0.121144])

    names.append("RAnklePitch")
    times.append([0.96, 1.76, 2.56, 3.56, 4.72, 5.52, 7.16, 8.8])
    keys.append([0.1335, 0.147306, 0.147306, 0.147306, 0.147306, 0.147306, 0.136568, 0.12583])

    names.append("RAnkleRoll")
    times.append([0.96, 1.76, 2.56, 3.56, 4.72, 5.52, 7.16, 8.8])
    keys.append([0.397761, 0.397761, 0.397761, 0.397761, 0.397761, 0.397761, 0.397761, 0.397761])

    names.append("RElbowRoll")
    times.append([0.96, 1.76, 2.56, 3.56, 4.72, 5.52, 7.16, 8.8])
    keys.append([0.227074, 0.78545, 1.30854, 0.372804, 1.48802, 0.418824, 0.30224, 0.15651])

    names.append("RElbowYaw")
    times.append([0.96, 1.76, 2.56, 3.56, 4.72, 5.52, 7.16, 8.8])
    keys.append([0.4801, 2.08567, 2.08567, 2.01717, 2.08567, 2.08567, 1.91592, 1.45572])

    names.append("RHand")
    times.append([0.96, 1.76, 2.56, 3.56, 4.72, 5.52, 7.16, 8.8])
    keys.append([0.454, 0.454, 0.454, 0.454, 0.454, 0.454, 0.454, 0.454])

    names.append("RHipPitch")
    times.append([0.96, 1.76, 2.56, 3.56, 4.72, 5.52, 7.16, 8.8])
    keys.append([0.371186, 0.420274, 0.44175, 0.481634, 0.481634, 0.481634, 0.481634, 0.48398])

    names.append("RHipRoll")
    times.append([0.96, 1.76, 2.56, 3.56, 4.72, 5.52, 7.16, 8.8])
    keys.append([-0.667248, -0.704064, -0.704064, -0.704064, -0.704064, -0.704064, -0.73321, -0.73321])

    names.append("RHipYawPitch")
    times.append([0.96, 1.76, 2.56, 3.56, 4.72, 5.52, 7.16, 8.8])
    keys.append([-0.420274, -0.4034, -0.392662, -0.377322, -0.377322, -0.377322, -0.377322, -0.377322])

    names.append("RKneePitch")
    times.append([0.96, 1.76, 2.56, 3.56, 4.72, 5.52, 7.16, 8.8])
    keys.append([-0.0923279, -0.0923279, -0.0923279, -0.0923279, -0.0923279, -0.0923279, -0.0923279, -0.0923279])

    names.append("RShoulderPitch")
    times.append([0.96, 1.76, 2.56, 3.56, 4.72, 5.52, 7.16, 8.8])
    keys.append([1.41132, 1.2886, 0.788518, 0.874422, 0.859082, 0.860616, 1.16281, 1.66903])

    names.append("RShoulderRoll")
    times.append([0.96, 1.76, 2.56, 3.56, 4.72, 5.52, 7.16, 8.8])
    keys.append([-0.253152, -0.909704, -1.28707, -1.32645, -1.31928, -1.31928, -0.783916, -0.291502])

    names.append("RWristYaw")
    times.append([0.96, 1.76, 2.56, 3.56, 4.72, 5.52, 7.16, 8.8])
    keys.append([-0.466378, -0.454106, -0.316046, -0.197928, -0.197928, -0.197928, -0.316046, -0.81613])

    try:
      # uncomment the following line and modify the IP if you use this script outside Choregraphe.
      motion = ALProxy("ALMotion", "138.67.236.222", 9559)
      # motion = ALProxy("ALMotion")
      motion.angleInterpolation(names, keys, times, True)
    except BaseException, err:
      print err



    # Go to rest position
    motion_service.rest()


if __name__ == "__main__":
    #parser = argparse.ArgumentParser()
    #parser.add_argument("--ip", type=str, default=,
    #                    help="Robot IP address. On robot or Local Naoqi: use '127.0.0.1'.")
    #parser.add_argument("--port", type=int, default=9559,
     #                   help="Naoqi port number")

    #args = parser.parse_args()
    session = qi.Session()
    try:
        session.connect("tcp://" + "138.67.236.222" + ":" + str(9559))
    except RuntimeError:
        print ("Can't connect to Naoqi at ip \"" + args.ip + "\" on port " + str(args.port) +".\n"
               "Please check your script arguments. Run with -h option for help.")
        sys.exit(1)
    main(session)



