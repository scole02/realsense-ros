#!/usr/bin/env python

import rospy
from sensor_msgs.msg import PointCloud2
from std_msgs.msg import Header

class TimeRepublisher:
    def __init__(self):
        rospy.init_node('time_republisher', anonymous=True)
        # Read parameters from ROS parameter server
        image_topic = rospy.get_param('~image_topic', "/default")
        print("Republishing image topic from: " + image_topic)
        republished_image_topic = rospy.get_param('~republished_image_topic', "/default")
        print("Republishing image topic to: " + republished_image_topic)
        self.image_sub = rospy.Subscriber(image_topic, PointCloud2, self.image_callback)
        self.image_pub = rospy.Publisher(republished_image_topic, PointCloud2, queue_size=10)

    def image_callback(self, data: PointCloud2):
        # Get the current simulated time from /clock
        current_time = rospy.get_rostime()
        
        # Update the header timestamp of the image message
        data.header.stamp = current_time
        data.header.frame_id = "camera_link"
        
        # Publish the image with simulated time
        self.image_pub.publish(data)

if __name__ == '__main__':
    
    # Initialize the TimeRepublisher node
    
    tr = TimeRepublisher()
    
    rospy.spin()
