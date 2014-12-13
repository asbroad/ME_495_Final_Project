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


class  vertical_calibration():
	def __init__(self, error):
		self.error = error
		self.pub = rospy.Publisher('calibration/pose_y',String)
	
	def callback_CalibrateDistance_Yaxis(self, alvarMsg):
		print '\nTAGS DETECTED: ',len(alvarMsg.markers) 

		markers = alvarMsg.markers

		if len(markers) > 0:
			middleBlockIndex = len(markers) / 2
			if len(markers) % 2 == 0:
				block1Pos = markers[middleBlockIndex-1].pose.pose.position
				block2Pos = markers[middleBlockIndex].pose.pose.position

				z = block1Pos.z + block2Pos.z

				y = float(block1Pos.y + block2Pos.y) / 2
			else:
				blockPos = markers[middleBlockIndex].pose.pose.position

				z = blockPos.z
				y = blockPos.y

			print 'z = ',z,'  |  y = ',y
			if z + self.error >= 0 and z - self.error <= 0 and y + self.error >= 0 and y - self.error <= 0:
				pub.publish('calibrated')



	def CalibrateDistance_Xaxis(self):
		print 'Calibrating distance x-axis...'
		rospy.init_node('vision_calibration_x_axis')
		rospy.Subscriber("/ar_pose_marker",AlvarMarkers,self.callback_CalibrateDistance_Yaxis)
		rospy.sleep(100)
		rospy.spin()


if __name__ == '__main__':
	error = 0.009

	vision = vertical_calibration(error)
	vision.CalibrateDistance_Xaxis()
    