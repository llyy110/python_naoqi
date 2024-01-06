# -*- coding:utf-8 -*-
import threading
import naoqi
import subprocess
import time
from naoqi import ALProxy
import motion
# import almath
import qi
import argparse
import sys
import time


def main(ip):
    """
    Use ALBehaviorManager Module.
    """
    # Get the service ALBehaviorManager.

    session = qi.Session()
    try:
        session.connect("tcp://" + ip + ":" + str(9559))
    except RuntimeError:
        print ("Can't connect to Naoqi at i Please check your script arguments. Run with -h option for help.")
        sys.exit(1)
    behavior_mng_service = session.service("ALBehaviorManager")

    getBehaviors(behavior_mng_service)
    # launchAndStopBehavior(behavior_mng_service, 'untitled-60b53b/behavior_1')
    # defaultBehaviors(behavior_mng_service, behavior_name)
    # behavior_mng_service.stopBehavior('taichidance/behavior_1')
    # #太极五
    # behavior_mng_service.runBehavior('taichidance', _async=True)
    # time.sleep(60)
    #misterfunk舞蹈
    # behavior_mng_service.runBehavior('misterfunk', _async=True)

    # 停止太极五
    # behavior_mng_service.stopBehavior('taichidance')
    # 停止misterfunk
    behavior_mng_service.stopBehavior('misterfunk')


    # behavior_mng_service.runBehavior('untitled-60b53b/behavior_1')


def getBehaviors(behavior_mng_service):
    """
    Know which behaviors are on the robot.
    """

    names = behavior_mng_service.getInstalledBehaviors()
    print "Behaviors on the robot:"
    print names

    names = behavior_mng_service.getRunningBehaviors()
    print "Running behaviors:"
    print names

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
            print "Behavior is already running."

    else:
        print "Behavior not found."
    return

    names = behavior_mng_service.getRunningBehaviors()
    print "Running behaviors:"
    print names

    # Stop the behavior.
    if (behavior_mng_service.isBehaviorRunning(behavior_name)):
        behavior_mng_service.stopBehavior(behavior_name)
        time.sleep(1.0)
    else:
        print "Behavior is already stopped."

    names = behavior_mng_service.getRunningBehaviors()
    print "Running behaviors:"
    print names

def defaultBehaviors(behavior_mng_service, behavior_name):
    """
    Set a behavior as default and remove it from default behavior.
    """

    # Get default behaviors.
    names = behavior_mng_service.getDefaultBehaviors()
    print "Default behaviors:"
    print names

    # Add behavior to default.
    behavior_mng_service.addDefaultBehavior(behavior_name)

    names = behavior_mng_service.getDefaultBehaviors()
    print "Default behaviors:"
    print names

    # Remove behavior from default.
    behavior_mng_service.removeDefaultBehavior(behavior_name)

    names = behavior_mng_service.getDefaultBehaviors()
    print "Default behaviors:"
    print names


if __name__ == "__main__":  # 定义三台机器人的IP地址和端口号
    robot1_ip = "192.168.1.108"
    # robot1_port = 9559
    robot2_ip = "192.168.1.122"
    robot2_port = 9559
    robot3_ip = "192.168.1.125"
    robot3_port = 9559  # 创建三个线程来控制三台机器人
    thread1 = threading.Thread(target=main, args=(robot1_ip,))
    thread2 = threading.Thread(target=main, args=(robot2_ip,))
    thread3 = threading.Thread(target=main, args=(robot3_ip,))  # 启动线程
    thread1.start()
    thread2.start()
    thread3.start()
    # main(robot3_ip)