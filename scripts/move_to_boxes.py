#!/usr/bin/env python

import roslib; roslib.load_manifest('youbot_nav_msr')
import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan


class Simple_P_Controller(object):

    def __init__(self):
    	
	rospy.init_node('simple_p_controller')
    	
	self._y_speed = 0.1  
        self._p = rospy.Publisher('cmd_vel', Twist)
    	rospy.Subscriber('scan', LaserScan, self.scan_callback, queue_size=1)

	self._reached_goal = False
        while not self._reached_goal:
	    rospy.spin()

    def scan_callback(self, scan):
	
	dist_from_box = scan.ranges[-1]
	print('Now : ' + str(dist_from_box) + ' meters from the box.')
	# create a twist message, fill in the details
    	twist = Twist()
	twist.linear.y = self._y_speed;
	if dist_from_box < 0.25:
	    twist.linear.y = 0
            self._reached_goal = True
    	    rospy.loginfo("Stopping!")
        else:
    	    rospy.loginfo("Moving!")
	
	self._p.publish(twist)
	rospy.sleep(0.1)


if __name__=="__main__":
    try:
       p = Simple_P_Controller()
    except rospy.ROSInterruptException:
       print('Failed to load proportional controller')

