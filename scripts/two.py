#!/usr/bin/env python3

import rospy
from std_msgs.msg import Int32

n = 0

def cb(message):
    global n
    n = message.data**2

if __name__ == '__main__':
    rospy.init_node('two')
    sub = rospy.Subscriber('count_up', Int32, cb)
    pub = rospy.Publisher('two', Int32, queue_size=1)
    rate = rospy.Rate(1)
    while not rospy.is_shutdown():
        pub.publish(n)
        rate.sleep()
