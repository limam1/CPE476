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
t_end = time.time() + 900
t_end1 = time.time() + 1
while True:
	linear_ms = 0
	rotate_rads = .2
	update_twist()	
	if t_end1 < time.time() :
		break

# stop motors and shut down light
romi.twist(0.0, 0.0)
romi.pixels(0, 0, 0)
