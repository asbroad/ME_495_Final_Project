#!/usr/bin/env python

import roslib; roslib.load_manifest('youbot_nav_msr')
import rospy
from youbot_nav_msr.msg import PosName
import sys

def send_named_goal():
    #initialize node
    rospy.init_node('send_named_goal')
    pub = rospy.Publisher('named_goal', PosName, queue_size=1) 
    
    pos_name = rospy.myargv(argv=sys.argv)[1]
    
    r = rospy.Rate(1)
    while not rospy.is_shutdown():
        pub.publish(pos_name) 
        r.sleep()

if __name__ == '__main__':
    try:
        send_named_goal()
    except rospy.ROSInterruptException:
        print "Keyboard Interrupt"
