from naoqi import ALProxy
motion = ALProxy("ALMotion", "138.67.236.222", 9559)
tts = ALProxy("ALTextToSpeech", "138.67.236.222", 9559)
motion.moveInit()
motion.post.moveTo(0.5, 0, 0)
tts.say("I'm walking")