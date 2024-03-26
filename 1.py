# coding=utf-8
import time

from naoqi import ALProxy


def main(motion):
    # motion = ALProxy("ALMotion", IP, PORT)
    # 步调参数
    config = [["MaxStepX", 0.16], ["MaxStepY", 0.16], ["MaxStepTheta", 0.5270], ["StepHeight", 0.015],
              ["MaxStepFrequency", 1]]
    standard = 90  # 巨大阈值, diff绝对值大于此值时认定为diff过大, 大范围转向  90
    straight = 9  # 直走阈值, diff绝对值小于此值时直走
    # todo 测试能否使用move和moveToward方法行走, 这两种方法为非阻塞调用方法
    # 左偏,需向右走
    # print "右转"
    # motion.post.moveTo(0.28, -0.0012455, 3 * 0.02 + 0.014, config)
    # 右偏,需向左走
    # print "左走"
    # motion.post.moveTo(0.32712, 0.000934575, 3 * 0.0366, config)
    # 左偏较大,需向右走
    print "大范围右"
    motion.post.moveTo(0.08, 0, -3.3, config)
    # time.sleep(1)
    print "直走"
    motion.post.moveTo(0.3975, -0.0034125, -0.0014*1.5, config)
    #
    # print "大范围左"
    # motion.post.moveTo(0.08, 0, 0.5, config)
    # <---* time: 1'20" *--->


if __name__ == '__main__':
    config = [["MaxStepX", 0.16], ["MaxStepY", 0.16], ["MaxStepTheta", 0.5270], ["StepHeight", 0.015],
              ["MaxStepFrequency", 1]]
    motion = ALProxy("ALMotion", '192.168.3.121', 9559)
    motion.post.moveTo(0.2, 0, -3.0, config)
    time.sleep(7)
    motion.post.moveTo(2, 0, -0.0006, config)
    # time.sleep(2)