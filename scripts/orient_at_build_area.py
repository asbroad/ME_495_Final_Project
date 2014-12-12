#!/usr/bin/env python

import roslib; roslib.load_manifest('youbot_nav_msr')
import rospy
import actionlib
from move_base_msgs.msg import *
from geometry_msgs.msg import Twist

def move_to_collection_area():

    #Simple Action Client - The simple action client is used to send actions to the
    #robot through a system of "goals". Here, we are setting the parameters as a 
    #move_base goal, which is in charge of moving the robot. 
    sac = actionlib.SimpleActionClient('move_base', MoveBaseAction)

    #create goal
    goal = MoveBaseGoal()
    #set goal
    goal.target_pose.pose.position.x = 0.352 
    goal.target_pose.pose.position.y = -0.440
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

if __name__=='__main__':
    
    #initialize node
    rospy.init_node('orient_at_build_area')

    move_to_collection_area()
    help_localize()
    move_to_collection_area()
    print('FINISHED')


