#!/usr/bin/env python

import roslib; roslib.load_manifest('youbot_nav_msr')
import rospy
import actionlib
from move_base_msgs.msg import *
from youbot_nav_msr.msg import PosName

def goal_name_callback(data):
    goal_name = str(data.pos_name)
    if rospy.has_param(goal_name):
        full_goal_pos = rospy.get_param(goal_name)	

        #Simple Action Client - The simple action client is used to send actions to the
        #robot through a system of "goals". Here, we are setting the parameters as a 
        #move_base goal, which is in charge of moving the robot. 
        sac = actionlib.SimpleActionClient('move_base', MoveBaseAction)

        #create goal
        goal = MoveBaseGoal()
        #set goal
        goal.target_pose.pose.position.x = float(full_goal_pos.get('pos_x'))
        goal.target_pose.pose.position.y = float(full_goal_pos.get('pos_y'))
        goal.target_pose.pose.position.z = float(full_goal_pos.get('pos_z'))
        goal.target_pose.pose.orientation.w = float(full_goal_pos.get('orient_w'))
        goal.target_pose.pose.orientation.x = float(full_goal_pos.get('orient_x'))
        goal.target_pose.pose.orientation.y = float(full_goal_pos.get('orient_y'))
        goal.target_pose.pose.orientation.z = float(full_goal_pos.get('orient_z'))

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

    else:
        print('The parameter server is not aware of a location named : ' + goal_name)


def semantic_nav():
    #initialize node
    rospy.init_node('move_to_named_position')

    rospy.Subscriber('named_goal', PosName, goal_name_callback)
    #test_value = rospy.get_param('collection_area')	
    #print(test_value)
    rospy.spin()

if __name__ == '__main__':
    try:
        semantic_nav()
    except rospy.ROSInterruptException:
        print "Keyboard Interrupt"
