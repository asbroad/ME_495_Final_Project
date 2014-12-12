#!/usr/bin/env python

""" Example code of how to move a robot forward for 3 seconds. """

# We always import roslib, and load the manifest to handle dependencies
import roslib; roslib.load_manifest('youbot_nav_msr')
import rospy

# recall: robots generally take base movement commands on a topic 
#  called "cmd_vel" using a message type "geometry_msgs/Twist"
from geometry_msgs.msg import Twist

rotate_speed = 0.3  # 0.1 m/s

# this quick check means that the following code runs ONLY if this is the 
# main file -- if we "import move" in another file, this code will not execute.
if __name__=="__main__":

    # first thing, init a node!
    rospy.init_node('move')

    # publish to cmd_vel
    p = rospy.Publisher('cmd_vel', Twist)

    direction = rospy.get_param('/direction',1)

    # create a twist message, fill in the details
    twist = Twist()
    twist.linear.x = 0;                   # our forward speed
    twist.linear.y = 0; twist.linear.z = 0;     # we can't use these!        
    twist.angular.x = 0; twist.angular.y = 0;   #          or these!
    twist.angular.z = rotate_speed;                        # no rotation

    # announce move, and publish the message
    rospy.loginfo("About to be moving!")
    for i in range(200):
        p.publish(twist)
        rospy.sleep(0.1) # 30*0.1 = 3.0
    
    # create a new message
    twist = Twist()

    # note: everything defaults to 0 in twist, if we don't fill it in, we stop!
    rospy.loginfo("Stopping!")
    p.publish(twist)
