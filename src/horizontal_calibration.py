#!/usr/bin/env python

import rospy
import math
import tf
from geometry_msgs.msg import (
	PoseStamped,
	Pose,
	Point,
	Quaternion,
)
from ar_track_alvar_msgs.msg import AlvarMarkers,AlvarMarker
from std_msgs.msg import String
import rospy



class horizontal_calibration():
	def __init__(self, calibration_dist_x, error):
		self.calibration_dist_x = calibration_dist_x
		self.error = error
		self.pub = rospy.Publisher('calibration/pose_x',String)
	
	def callback_CalibrateDistance_Xaxis(self, alvarMsg):
		print '\nTAGS DETECTED: ',len(alvarMsg.markers) 
		for marker in alvarMsg.markers:
			print marker.id
			position = marker.pose.pose.position
			print '\nX = ', position.x
			if position.x + self.error >= self.calibration_dist_x and position.x - self.error <= self.calibration_dist_x:
				pub.publish('calibrated')

	def CalibrateDistance_Xaxis(self):
		print 'Calibrating distance x-axis...'
		rospy.init_node('vision_calibration_x_axis')
		rospy.Subscriber("/ar_pose_marker",AlvarMarkers,self.callback_CalibrateDistance_Xaxis)
		rospy.sleep(100)
		rospy.spin()


if __name__ == '__main__':
	error = 0.009

	calibration_dist_x = 0.240
	calibration_dist_y = -0.0734
	calibration_dist_z = -0.0115
	vision = horizontal_calibration(calibration_dist_x, error)
	vision.CalibrateDistance_Xaxis()
    