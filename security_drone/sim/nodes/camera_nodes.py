#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2

class CameraNode(Node):
    def __init__(self):
        super().__init__('camera_node')
        self.pub = self.create_publisher(Image, '/camera/image_raw', 10)
        self.bridge = CvBridge()
        self.cap = cv2.VideoCapture(0)  # change to Gazebo later
        self.timer = self.create_timer(0.033, self.timer_callback)  # 30 Hz

    def timer_callback(self):
        ret, frame = self.cap.read()
        if ret:
            msg = self.bridge.cv2_to_imgmsg(frame, encoding='bgr8')
            self.pub.publish(msg)

def main():
    rclpy.init()
    node = CameraNode()
    rclpy.spin(node)

if __name__ == '__main__':
    main()