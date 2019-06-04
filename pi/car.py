import RPi.GPIO as GPIO
import time
import pygame

""" pygame初始化 """
pygame.init()
screen = pygame.display.set_mode((200, 200))
pygame.display.set_caption("Car")

""" 指定GPIO口 """
GPIO.setmode(GPIO.BCM)
GPIO.setup(26, GPIO.OUT)
GPIO.setup(19, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(6, GPIO.OUT)
GPIO.setup(20, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)
ENA = 26
ENB = 19
INA = 13
INB = 6
INC = 20
IND = 16


""" 设置正转 """
GPIO.output(INB, True)
GPIO.output(INA, False)
GPIO.output(IND, True)
GPIO.output(INC, False)

""" 初始化PWM, 控制速度 """
pwm_l = GPIO.PWM(ENA, 50)
pwm_r = GPIO.PWM(ENB, 50)
speed = 0
speed_up = 1   # 速度增量
pwm_l.start(speed)
pwm_r.start(speed)


def speedup(pwm_l, pwm_r, speed):
    """ 加速 """
    if speed < 100:
        speed += speed_up
        pwm_l.ChangeDutyCycle(speed)
        pwm_r.ChangeDutyCycle(speed)
    else:
        pwm_l.ChangeDutyCycle(speed)
        pwm_r.ChangeDutyCycle(speed)
    time.sleep(0.2)
    return speed


def left(pwm_l, pwm_r, speed):
    """ 左转 """
    pwm_l.ChangeDutyCycle(speed / 2)


def right(pwm_l, pwm_r, speed):
    """ 右转 """
    pwm_r.ChangeDutyCycle(speed / 2)


""" 插旗 """
speedup_flag = False
stop_flag = False
left_flag = False
right_flag = False


while True:
    for event in pygame.event.get():
        """ 按下按键 """
        if event.type == pygame.KEYDOWN:
            # 按下空格
            if event.key == pygame.K_SPACE:
                stop_flag = not stop_flag
            # 按下 W
            if event.key == pygame.K_w:
                speedup_flag = True
            # 按下 A
            if event.key == pygame.K_a:
                left_flag = True
            # 按下 D
            if event.key == pygame.K_d:
                right_flag = True
        """ 弹起按键 """
        if event.type == pygame.KEYUP:
            # 弹起空格
            if event.key == pygame.K_SPACE:
                stop_flag = not stop_flag
            # 弹起W
            if event.key == pygame.K_w:
                speedup_flag = False
            # 弹起 A
            if event.key == pygame.K_a:
                left_flag = False
            # 弹起 D
            if event.key == pygame.K_d:
                right_flag = False

    """ 改变小车状态 """
    if left_flag:
        left(pwm_l, pwm_r, speed)
    elif right_flag:
        right(pwm_l, pwm_r, speed)
    elif speedup_flag:
        speed = speedup(pwm_l, pwm_r, speed)
    elif stop_flag:
        pwm_l.ChangeDutyCycle(0)
        pwm_r.ChangeDutyCycle(0)
    else:
        speedup(pwm_l, pwm_r, speed)   # 不按键时维持速度
