#!/usr/bin/env python

import roslib; roslib.load_manifest('youbot_nav_msr')
import rospy
import actionlib
from move_base_msgs.msg import *
from geometry_msgs.msg import Twist

'''
This script will move to the collection area defined in the /map frame.  It will first set a nav goal (again, 
as defined in the /map frame and move to that location.  As the area we are working in does not allow
for the best localization with current techniques, we then try to improve our localization by rotating 360
degrees in place. We then resend the original desired position which helps correct any error in the original
position.
'''

def move_to_collection_area():

    #Simple Action Client - The simple action client is used to send actions to the
    #robot through a system of "goals". Here, we are setting the parameters as a 
    #move_base goal, which is in charge of moving the robot. 
    sac = actionlib.SimpleActionClient('move_base', MoveBaseAction)

    #create goal
    goal = MoveBaseGoal()
    #set goal
    # THIS GOAL CAN BE EASILY CHANGED IF WE WERE TO MOVE THE BOXES OR EXTEND THIS PROJECT TO DIFFERENT MAP
    goal.target_pose.pose.position.x = 0.252 
    goal.target_pose.pose.position.y = 0.660
    goal.target_pose.pose.position.z = 0.000
    goal.target_pose.pose.orientation.x = 0.000
    goal.target_pose.pose.orientation.y = 0.000
    goal.target_pose.pose.orientation.z = -0.713
    goal.target_pose.pose.orientation.w = 0.701

    goal.target_pose.header.frame_id = 'map'
    goal.target_pose.header.stamp = rospy.Time.now()

    print(goal)

    #start listener
    sac.wait_for_server()
    #send goal
    sac.send_goal(goal)

    #finish
    sac.wait_for_result()

    #print result
    print sac.get_result()

def help_localize():

    rotate_speed = 0.3  # 0.1 m/s

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
    
    # stop spinning
    twist = Twist()
    rospy.loginfo("Stopping!")
    p.publish(twist)

if __name__=='__main__':
    
    #initialize node
    rospy.init_node('orient_at_collection_area')

    move_to_collection_area()
    help_localize()
    move_to_collection_area()
    print('FINISHED')


