# -*- coding: utf-8 -*-
from naoqi import ALProxy
from time import sleep
import almath

tts = ALProxy("ALTextToSpeech", "192.168.1.134", 9559)
TTS = ALProxy("ALMotion", "192.168.1.134", 9559)
tts1 = ALProxy("ALTextToSpeech", "192.168.1.114", 9559)
TTS1 = ALProxy("ALMotion", "192.168.1.114", 9559)
tts.setLanguage("Chinese")
tts1.say("老师们好")

tts.say('老师们好，请欣赏我们准备的情景短剧<初相识>')

tts1.say("你好")

TTS1.setStiffnesses("Body", 1.0)
names = "RShoulderPitch"
angels = 10.0 * almath.TO_RAD
fractionMaxSpeed = 0.8
TTS1.setAngles(names, angels, fractionMaxSpeed)
TTS1.setStiffnesses("Body", 1.0)
names = "RElbowRoll"
angels = 60.0 * almath.TO_RAD
fractionMaxSpeed = 0.8
TTS1.setAngles(names, angels, fractionMaxSpeed)
sleep(1)
TTS1.setStiffnesses("Body", 1.0)
names = "RShoulderPitch"
angels = 70.0 * almath.TO_RAD
fractionMaxSpeed = 0.8
TTS1.setAngles(names, angels, fractionMaxSpeed)
TTS1.setStiffnesses("Body", 1.0)
names = "RElbowRoll"
angels = -10.0 * almath.TO_RAD
fractionMaxSpeed = 0.8
TTS1.setAngles(names, angels, fractionMaxSpeed)
tts.say("Hello")
TTS.setStiffnesses("Body", 1.0)
names = "RShoulderPitch"
angels = -10.0 * almath.TO_RAD
fractionMaxSpeed = 0.8
TTS.setAngles(names, angels, fractionMaxSpeed)
TTS.setStiffnesses("Body", 1.0)
names = "RElbowRoll"
angels = 60.0 * almath.TO_RAD
fractionMaxSpeed = 0.8
TTS.setAngles(names, angels, fractionMaxSpeed)
sleep(1)
TTS.setStiffnesses("Body", 1.0)
names = "RShoulderPitch"
angels = 70.0 * almath.TO_RAD
fractionMaxSpeed = 0.8
TTS.setAngles(names, angels, fractionMaxSpeed)

TTS.setStiffnesses("Body", 1.0)
names = "RElbowRoll"
angels = -10.0 * almath.TO_RAD
fractionMaxSpeed = 0.8
TTS.setAngles(names, angels, fractionMaxSpeed)

tts1.say("你叫什么名字")
tts.say("我的名字叫小黄")
tts1.say("你多大了")
tts.say("问别人的年龄不礼貌")
tts1.say("那你告诉我你的编码是多少呗")
tts.say("我的编码是192.168.134.98")
tts.say("你的编码是多少")
tts1.say("我的编码是192.168.134.50")
tts1.say("你可以说一段绕口令吗")
tts.say("满足你")
tts.say("白石白又滑，搬来白石搭白塔。")
tts.say("白石塔，白石塔，")
tts.say("白石搭石塔，白塔白石搭")
tts.say("搭好白石塔，白塔白又滑")
tts.say("你也说一个绕口令给我听一听")
tts1.say("那我给你说一个")
tts1.say("八百标兵奔北坡，炮兵并排北边跑。")
tts1.say("炮兵怕把标兵碰，标兵怕碰炮兵炮。")
tts1.say("小黄我说的怎么样")
tts.say("你说的相当的不错")
tts1.say("你说的也很好")
tts.say("你还没有告诉我你叫什么名字")
tts1.say("我的名字叫小名")
tts.say("很高兴认识你，小名")
tts1.say("我也很高兴认识你")
# tts1.say("你可以给我唱首歌吗")
tts1.say("我是人型机器人nao来自日本 目前我们有很多个伙伴在世界各地")
tts.say("下面让我们另外的伙伴为你们跳个舞吧")

#
# tts.say("郎恋娘来娘念郎")
# tts.say("念娘恋娘")
# tts.say("念郎恋郎")
# tts.say("念恋娘郎")
