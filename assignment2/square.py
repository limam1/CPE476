#!/usr/bin/python2
#
# Move the robot forwards and backwards
from romipi_astar.romipi_driver import AStar
import time

romi = AStar()
linear_ms = 0.0
rotate_rads = 0.0


def update_twist():
    """send twist to driver and change light color if moving"""
    if linear_ms == 0.0 and rotate_rads == 0.0:
        romi.pixels(0, 0, 100)
    else:
        romi.pixels(0, 100, 0)
    romi.twist(linear_ms, rotate_rads)


# all set up, now run the robot
i = 0
while True:
    # straight
    t_end = time.time() + 1
    while t_end > time.time() :
        print ("Straight")
        linear_ms = .2
        rotate_rads = 0
        update_twist()
    # turn
    t_end = time.time() + 1
    while t_end > time.time() :
        print ("Turn")
        linear_ms = 0
        rotate_rads = 0.2
        update_twist()
    if i == 4 :
        break
    else :
        i = i + 1

# stop motors and shut down light
romi.twist(0.0, 0.0)
romi.pixels(0, 0, 0)
