#!/usr/bin/env python

""" 
This script will rotate the youBot in place for 360 degrees.  We use this script to improve
our localization efforts. 
"""

import roslib; roslib.load_manifest('youbot_nav_msr')
import rospy
from geometry_msgs.msg import Twist

rotate_speed = 0.3  

if __name__=="__main__":

    rospy.init_node('rotate_in_place')

    # publish to cmd_vel
    p = rospy.Publisher('cmd_vel', Twist)

    # create a twist message, fill in the details
    twist = Twist()
    twist.linear.x = 0;                  
    twist.linear.y = 0; twist.linear.z = 0;    
    twist.angular.x = 0; twist.angular.y = 0; 
    twist.angular.z = rotate_speed;          

    # announce move, and publish the message
    rospy.loginfo("About to be moving!")
    for i in range(200):
        p.publish(twist)
        rospy.sleep(0.1) 
    
    # stop moving
    twist = Twist()
    rospy.loginfo("Stopping!")
    p.publish(twist)
