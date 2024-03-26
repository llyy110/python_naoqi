# coding=utf-8
import argparse
import time
import qi
import yaml
from naoqi import ALProxy

session = qi.Session


# 函数：初始化机器人连接
def init_robots(conf_file):

    with open(conf_file, 'r') as file:
        config = yaml.safe_load(file)
    robots = {}
    mm = []
    for idx, robot_conf in config['nao'].items():
        mm.append(idx)
        ip = robot_conf['ip']
        port = robot_conf['port']
        robots = ALProxy("ALMotion", ip, port)
    return mm, robots


# 函数：机器人移动
def move_robot(robots, ids, direction, steps):
    for idx in ids:
        robot = robots[idx]
        if direction == 'W':
            robot.moveForward(steps)
        elif direction == 'S':
            robot.moveBackward(steps)
        elif direction == 'A':
            robot.moveLeft(steps)
        elif direction == 'D':
            robot.moveRight(steps)
        robot.waitUntilMoveIsFinished()

    # 函数：机器人蹲起


def crouch_robot(robots, ids, times):
    for idx in ids:
        robot = robots[idx]
        for _ in range(times):
            robot.crouch()
            robot.stand()

        # 函数：机器人说话


def say_robot(robots, ids, text):
    for idx in ids:
        robot = robots[idx]

        # 获取ALTextToSpeech服务的代理
        tts = session.service("ALTextToSpeech", robot[idx].getIP(), robot[idx].getPort())

        # 让NAO机器人说话
        text_to_say = "你好，我是NAO机器人，我会说话！"  # 替换成你想让NAO说的文本
        tts.say(text_to_say)

        # 等待一段时间让NAO说完话
        time.sleep(2)

        # 关闭会话
        session.close()

    # 函数：获取机器人的动作列表


def get_animations(robots, ids):
    for idx in ids:
        robot = robots[idx]
        animations = robot.getAnimationList()
        print("Robot %d animations: %s" % (idx, animations))

    # 函数：执行机器人的动作


def execute_animation(robots, ids, animation_name):
    for idx in ids:
        robot = robots[idx]
        try:
            robot.runAnimation(animation_name)
        except Exception as e:
            print("Error executing animation '{animation_name}' on robot {idx}: {e}")

        # 主函数



def main():
    # 配置文件路径
    config_file = 'conf.yaml'

    # 加载配置
    idxx, robot = init_robots(config_file)

    parser = argparse.ArgumentParser(description='NAOqi tool to control NAO robots')
    parser.add_argument('-c', '--conf', type=str, required=True, help='Path to the configuration file')
    parser.add_argument('-n', '--robot-ids', type=str, default='', help='Comma-separated list of robot IDs to control')
    parser.add_argument('-W', '--forward', type=int, help='Move forward a number of steps')
    parser.add_argument('-S', '--backward', type=int, help='Move backward a number of steps')
    parser.add_argument('-A', '--left', type=int, help='Move left a number of steps')
    parser.add_argument('-D', '--right', type=int, help='Move right a number of steps')
    parser.add_argument('-Z', '--crouch', type=int, help='Crouch a number of times')
    parser.add_argument('--say', type=str, help='Text to speak')
    parser.add_argument('-K', '--get-animations', action='store_true', help='Get the list of available animations')
    parser.add_argument('-N', '--animation', type=str, help='Run a specific animation')
    args = parser.parse_args()

    robots = init_robots(args.conf)
    ids = idxx

    if args.forward:
        move_robot(robots, ids, 'W', args.forward)
    elif args.backward:
        move_robot(robots, ids, 'S', args.backward)
    elif args.leftward:
        move_robot(robots, ids, 'A', args.backward)
    elif args.rightward:
        move_robot(robots, ids, 'D', args.backward)


"""
python naoqifengzhuang -c conf.yaml -W 10

C:\Users\35472\PycharmProjects\python_naoqi\naoqifengzhuang.exe
"""

if __name__ == '__main__':
    main()