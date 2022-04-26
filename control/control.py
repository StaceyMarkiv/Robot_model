#!/usr/bin/env python
import rospy
import time
from std_msgs.msg import Float64

pub_wheel_1_left = rospy.Publisher('/my_bot/wheel_1_left_joint_position_controller', Float64, queue_size=10)
pub_wheel_2_left = rospy.Publisher('/my_bot/wheel_2_left_joint_position_controller', Float64, queue_size=10)
pub_wheel_3_left = rospy.Publisher('/my_bot/wheel_3_left_joint_position_controller', Float64, queue_size=10)
pub_wheel_1_right = rospy.Publisher('/my_bot/wheel_1_right_joint_position_controller', Float64, queue_size=10)
pub_wheel_2_right = rospy.Publisher('/my_bot/wheel_2_right_joint_position_controller', Float64, queue_size=10)
pub_wheel_3_right = rospy.Publisher('/my_bot/wheel_3_right_joint_position_controller', Float64, queue_size=10)
pub_left_shoulder_forward = rospy.Publisher('/my_bot/left_shoulder_forward_joint_position_controller', Float64, queue_size=10)
pub_left_center = rospy.Publisher('/my_bot/left_center_joint_position_controller', Float64, queue_size=10)
pub_right_shoulder_forward = rospy.Publisher('/my_bot/right_shoulder_forward_joint_position_controller', Float64, queue_size=10)
pub_right_center = rospy.Publisher('/my_bot/left_center_right_position_controller', Float64, queue_size=10)
pub_neck = rospy.Publisher('/my_bot/neck_joint_position_controller', Float64, queue_size=10)

rospy.init_node('mybot_control')
r = rospy.Rate(10)
time.sleep(3)
wheel_1_left_msg = 0
wheel_2_left_msg = 0
wheel_3_left_msg = 0
wheel_1_right_msg = 0
wheel_2_right_msg = 0
wheel_3_right_msg = 0
left_shoulder_forward_msg = 0
left_center_msg = 0
right_shoulder_forward_msg = 0
right_center_msg = 0
neck_msg = 0

while not rospy.is_shutdown():
    wheel_1_left_msg += 0.010
    wheel_2_left_msg += 0.011
    wheel_3_left_msg += 0.012
    wheel_1_right_msg += 0.013
    wheel_2_right_msg += 0.014
    wheel_3_right_msg += 0.015
    left_shoulder_forward_msg += 0.016
    left_center_msg += 0.017
    right_shoulder_forward_msg += 0.018
    right_center_msg += 0.019
    neck_msg += 0.020

    pub_wheel_1_left.publish(wheel_1_left_msg)
    pub_wheel_2_left.publish(wheel_2_left_msg)
    pub_wheel_3_left.publish(wheel_3_left_msg)
    pub_wheel_1_right.publish(wheel_1_right_msg)
    pub_wheel_2_right.publish(wheel_2_right_msg)
    pub_wheel_3_right.publish(wheel_3_right_msg)
    pub_left_shoulder_forward.publish(left_shoulder_forward_msg)
    pub_left_center.publish(left_center_msg)
    pub_right_shoulder_forward.publish(right_shoulder_forward_msg)
    pub_right_center.publish(right_center_msg)
    pub_neck.publish(neck_msg)

    r.sleep()
    