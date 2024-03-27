# -*- coding:utf-8 -*-
import sys
import threading
from naoqi import ALProxy
import time

# import almath
import qi


def main(ip):
    """
    Use ALBehaviorManager Module.
    """
    # Get the service ALBehaviorManager.

    config = [["MaxStepX", 0.16], ["MaxStepY", 0.16], ["MaxStepTheta", 0.5270], ["StepHeight", 0.015],
              ["MaxStepFrequency", 1]]

    # tts1 = ALProxy("ALTextToSpeech", "192.168.3.124", 9559)
    # # TTS1 = ALProxy("ALMotion", "192.168.1.114", 9559)
    # tts1.setLanguage("Chinese")

    session = qi.Session()

    try:
        session.connect("tcp://" + ip + ":" + str(9559))
        motion = ALProxy("ALMotion", ip, 9559)

    except RuntimeError:
        print ("Can't connect to Naoqi at i Please check your script arguments. Run with -h option for help.")
        sys.exit(1)

    behavior_mng_service = session.service("ALBehaviorManager")
    getBehaviors(behavior_mng_service)
    # launchAndStopBehavior(behavior_mng_service, 'untitled-60b53b/behavior_1')
    # defaultBehaviors(behavior_mng_service, behavior_name)
    # behavior_mng_service.stopBehavior('taichidance/behavior_1')

    # 太极五
    behavior_mng_service.runBehavior('taichidance', _async=True)
    #
    # time.sleep(4)
    # tts1.say("老师们好，欢迎老师们到来，接下来，我们将为大家带来太极舞表演，"
    #          "由我来介绍太极舞，太极舞蹈是一种独特的舞蹈形式，它巧妙地将太极的哲学"
    #          "思想与舞蹈的优雅韵律相结合。舞者以柔和连贯的动作，"
    #          "表达太极的阴阳平衡与和谐之美，展现出一种内敛而深邃的艺术魅力。"
    #          "太极舞蹈不仅具有健身养生的功效，还能陶冶情操，提升人的气质与修养。")
    #
    # """
    #
    #          "回忆可以使人欢欣，但有的也不免使人寂寞，但唯有痛苦不能使人忘却，"
    #          "这便是呐喊一书的来由。但何为痛苦的记忆，是父亲生命垂危时药石无医的无奈，"
    # """
    #
    # # tts1.stop("192.168.3.126")
    # tts1.stopAll()
    #
    time.sleep(50)

    # misterfunk舞蹈
    # behavior_mng_service.runBehavior('misterfunk', _async=True)

    # 停止太极五
    behavior_mng_service.stopBehavior('taichidance')

    # 停止misterfunk
    # behavior_mng_service.stopBehavior('misterfunk')

    # behavior_mng_service.runBehavior('untitled-60b53b/behavior_1')

    motion.post.moveTo(0.2, 0, -3.0, config)
    time.sleep(7)
    motion.post.moveTo(2, 0, -0.0006, config)


def getBehaviors(behavior_mng_service):
    """
    Know which behaviors are on the robot.
    """

    names = behavior_mng_service.getInstalledBehaviors()
    print ("Behaviors on the robot:")
    print (names)

    names = behavior_mng_service.getRunningBehaviors()
    print("Running behaviors:")
    print(names)


def launchAndStopBehavior(behavior_mng_service, behavior_name):
    """
    Launch and stop a behavior, if possible.
    """
    # Check that the behavior exists.
    if (behavior_mng_service.isBehaviorInstalled(behavior_name)):
        # Check that it is not already running.
        if (not behavior_mng_service.isBehaviorRunning(behavior_name)):
            # Launch behavior. This is a blocking call, use _async=True if you do not
            # want to wait for the behavior to finish.
            behavior_mng_service.runBehavior(behavior_name, _async=True)
            time.sleep(0.5)
        else:
            print ("Behavior is already running.")

    else:
        print ("Behavior not found.")
    return

    names = behavior_mng_service.getRunningBehaviors()
    print ("Running behaviors:")
    print (names)

    # Stop the behavior.
    if (behavior_mng_service.isBehaviorRunning(behavior_name)):
        behavior_mng_service.stopBehavior(behavior_name)
        time.sleep(1.0)
    else:
        print ("Behavior is already stopped.")

    names = behavior_mng_service.getRunningBehaviors()
    print ("Running behaviors:")
    print (names)


def defaultBehaviors(behavior_mng_service, behavior_name):
    """
    Set a behavior as default and remove it from default behavior.
    """

    # Get default behaviors.
    names = behavior_mng_service.getDefaultBehaviors()
    print ("Default behaviors:")
    print (names)

    # Add behavior to default.
    behavior_mng_service.addDefaultBehavior(behavior_name)

    names = behavior_mng_service.getDefaultBehaviors()
    print ("Default behaviors:")
    print (names)

    # Remove behavior from default.
    behavior_mng_service.removeDefaultBehavior(behavior_name)

    names = behavior_mng_service.getDefaultBehaviors()
    print ("Default behaviors:")
    print (names)


if __name__ == "__main__":  # 定义三台机器人的IP地址和端口号
    robot1_ip = "192.168.3.126"  # 创建三个线程来控制三台机器人
    robot1_port = 9559
    robot2_ip = "192.168.3.122"
    robot2_port = 9559
    robot3_ip = "192.168.3.121"
    robot3_port = 9559
    # robot4_ip = "192.168.3.125"
    # robot4_port = 9559
    thread1 = threading.Thread(target=main, args=(robot1_ip,))  # 启动线程
    thread2 = threading.Thread(target=main, args=(robot2_ip,))
    thread3 = threading.Thread(target=main, args=(robot3_ip,))
    # thread4 = threading.Thread(target=main, args=(robot4_ip,))
    thread1.start()
    thread2.start()
    thread3.start()
    # thread4.start()
    # # main(robot3_ip)
