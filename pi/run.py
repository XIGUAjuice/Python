import RPi.GPIO as GPIO
import time
import pygame

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(19, GPIO.OUT)
GPIO.setup(26, GPIO.OUT)

EN_A = 22
IN_A = 27
IN_B = 17
EN_B = 26
IN_C = 13
IN_D = 19
sleep_time = 0.1


def forward():
    GPIO.output(EN_A, True)  # A使能
    GPIO.output(IN_A, True)
    GPIO.output(IN_B, False)

    GPIO.output(EN_B, True)  # B使能
    GPIO.output(IN_C, True)
    GPIO.output(IN_D, False)
    time.sleep(sleep_time)
    reset()


def backward():
    GPIO.output(EN_A, True)
    GPIO.output(IN_A, False)
    GPIO.output(IN_B, True)

    GPIO.output(EN_B, True)
    GPIO.output(IN_C, False)
    GPIO.output(IN_D, True)


def left():
    GPIO.output(EN_A, True)
    GPIO.output(IN_A, False)
    GPIO.output(IN_B, False)

    GPIO.output(EN_B, True)
    GPIO.output(IN_C, True)
    GPIO.output(IN_D, False)


def right():
    GPIO.output(EN_B, True)
    GPIO.output(IN_C, False)
    GPIO.output(IN_D, False)

    GPIO.output(EN_A, True)
    GPIO.output(IN_A, True)
    GPIO.output(IN_B, False)


# def back_left():
#     GPIO.output(EN_A, True)
#     GPIO.output(IN_A, False)
#     GPIO.output(IN_B, False)

#     GPIO.output(EN_B, True)
#     GPIO.output(IN_C, False)
#     GPIO.output(IN_D, True)


# def back_right():
#     GPIO.output(EN_A, True)
#     GPIO.output(IN_A, False)
#     GPIO.output(IN_B, True)

#     GPIO.output(EN_B, True)
#     GPIO.output(IN_C, False)
#     GPIO.output(IN_D, False)


def reset():
    GPIO.output(EN_A, False)
    GPIO.output(IN_A, False)
    GPIO.output(IN_B, False)

    GPIO.output(EN_B, False)
    GPIO.output(IN_C, False)
    GPIO.output(IN_D, False)


pygame.init()
screen = pygame.display.set_mode((200, 200))
pygame.display.set_caption("Alien Invasion")
forward_flag = False
backward_flag = False
left_flag = False
right_flag = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                forward_flag = True
            if event.key == pygame.K_s:
                backward_flag = True
            if event.key == pygame.K_a:
                left_flag = True
            if event.key == pygame.K_d:
                right_flag = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                forward_flag = False
            if event.key == pygame.K_s:
                backward_flag = False
            if event.key == pygame.K_a:
                left_flag = False
            if event.key == pygame.K_d:
                right_flag = False

    if forward_flag:
        forward()
    elif backward_flag:
        backward()
    elif left_flag:
        left()
    elif right_flag:
        right()
    else:
        reset()
