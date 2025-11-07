#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
from ultralytics import YOLO
import cv2

class YoloNode(Node):
    def __init__(self):
        super().__init__('yolo_node')
        self.model = YOLO('yolov8n.pt')  # 3 MB, 95 % accuracy
        self.sub = self.create_subscription(
            Image, '/camera/image_raw', self.callback, 10)
        self.bridge = CvBridge()

    def callback(self, msg):
        frame = self.bridge.imgmsg_to_cv2(msg, 'bgr8')
        results = self.model(frame, conf=0.5)
        annotated = results[0].plot()
        cv2.imshow('YOLO', annotated)
        cv2.waitKey(1)

def main():
    rclpy.init()
    node = YoloNode()
    rclpy.spin(node)

if __name__ == '__main__':
    main()