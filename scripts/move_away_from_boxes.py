#!/usr/bin/env python

""" 
This script will move the youBot a short distance in the negative direction along it's y-axis.
For our project, this is used to move the youBot away from the collection and building areas.
As it simply moves in the negative direction along it's y-axis, the youBot must have the box
it is moving away from on it's left side. 
"""

import roslib; roslib.load_manifest('youbot_nav_msr')
import rospy
from geometry_msgs.msg import Twist

y_speed = -0.1  

if __name__=="__main__":

    rospy.init_node('move_away_from_boxes')

    # publish to cmd_vel
    p = rospy.Publisher('cmd_vel', Twist)

    # create a twist message, fill in the details
    twist = Twist()
    twist.linear.y = y_speed;                   
    twist.linear.x = 0; twist.linear.z = 0;    
    twist.angular.x = 0; twist.angular.y = 0; 
    twist.angular.z = 0;                     

    # announce move, and publish the message
    rospy.loginfo("About to be moving!")
    for i in range(30):
        p.publish(twist)
        rospy.sleep(0.1) 
    
    # stop motion 
    twist = Twist()
    rospy.loginfo("Stopping!")
    p.publish(twist)
