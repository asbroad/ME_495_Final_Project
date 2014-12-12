#!/usr/bin/env python

""" 
This script will move the youBot a calculated distance between the collection and build areas.
It moves the youBot along it's x-axis. It can move the youBot either forwards or backwards,
depending on how the 'direction' parameter is set on the parameter server. If it isn't set, it
defaults to forwards.  This script is a basic version of our navigation implementation, in the end
we do not use this. It is about a simple as can get and therefore is not particularly extensible to
changes in the environment. We now use the ROS nav stack and other scripts in this directory to achieve
the same goal in a more robust manor.
"""

import roslib; roslib.load_manifest('youbot_nav_msr')
import rospy
from geometry_msgs.msg import Twist

x_speed = 0.1  

if __name__=="__main__":

    rospy.init_node('move_between_start_and_goal')

    # publish to cmd_vel
    p = rospy.Publisher('cmd_vel', Twist)

    direction = rospy.get_param('/direction',1)

    # create a twist message, fill in the details
    twist = Twist()
    twist.linear.x = direction*x_speed;        
    twist.linear.y = 0; twist.linear.z = 0;   
    twist.angular.x = 0; twist.angular.y = 0;
    twist.angular.z = 0;                    

    # announce move, and publish the message
    rospy.loginfo("About to be moving!")
    for i in range(110):
        p.publish(twist)
        rospy.sleep(0.1) # 30*0.1 = 3.0
    
    # stop motion
    twist = Twist()
    rospy.loginfo("Stopping!")
    p.publish(twist)
